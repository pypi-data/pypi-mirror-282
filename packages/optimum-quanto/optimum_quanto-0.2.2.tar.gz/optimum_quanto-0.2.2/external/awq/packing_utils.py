import torch


AWQ_ORDER = [0, 2, 4, 6, 1, 3, 5, 7]
AWQ_REVERSE_ORDER = [0, 4, 1, 5, 2, 6, 3, 7]


def pack_awq(intweight: torch.Tensor, reorder=False):
    bits = 4
    pack_num = 32 // bits
    qweight = torch.zeros(intweight.shape[0], intweight.shape[1] // pack_num, dtype=torch.int32, device=intweight.device)
    for col in range(intweight.shape[1] // pack_num):
        if reorder:
            order_map = [0, 2, 4, 6, 1, 3, 5, 7]
        else:
            order_map = [0, 1, 2, 3, 4, 5, 6, 7]
        for i in range(pack_num):
            qweight_col = intweight[:, col * pack_num + order_map[i]]
            qweight[:, col] |= qweight_col << (i * bits)
    return qweight


def unpack_awq(qweight: torch.Tensor, bits: int):
    shifts = torch.arange(0, 32, bits, device=qweight.device)

    # unpacking columnwise
    iweights = torch.bitwise_right_shift(qweight[:, :, None], shifts[None, None, :]).to(
        torch.int8  # smallest dtype available
    )
    iweights = iweights.view(iweights.shape[0], -1)

    return iweights


def reverse_awq_order(iweights: torch.Tensor, bits: int):
    reverse_order_tensor = torch.arange(
        iweights.shape[-1],
        dtype=torch.int32,
        device=iweights.device,
    )
    reverse_order_tensor = reverse_order_tensor.view(-1, 32 // bits)
    reverse_order_tensor = reverse_order_tensor[:, AWQ_REVERSE_ORDER]
    reverse_order_tensor = reverse_order_tensor.view(-1)

    iweights = iweights[:, reverse_order_tensor]

    return iweights


def pack_exllama(iweights: torch.Tensor, izeros: torch.Tensor, bits: int):
    shifts = torch.arange(0, 32, bits, device=iweights.device)

    # packing rowwise
    iweights = iweights.view(iweights.shape[0] // (32 // bits), 32 // bits, -1)
    qweight = (
        torch.bitwise_left_shift(iweights, shifts[None, :, None])
        .sum(dim=1)
        .to(torch.int32)
    )

    # packing columnwise
    izeros = izeros.view(-1, izeros.shape[1] // (32 // bits), 32 // bits)
    qzeros = (
        torch.bitwise_left_shift(izeros, shifts[None, None, :])
        .sum(dim=-1)
        .to(torch.int32)
    )

    return qweight, qzeros


def unpack_reorder_pack(qweight, qzeros, bits):
    # Unpack the qweight and qzeros tensors
    iweight, izeros = unpack_awq(qweight, qzeros, bits)
    # Reverse the order of the iweight and izeros tensors
    iweight, izeros = reverse_awq_order(iweight, izeros, bits)

    # overflow checks
    iweight = torch.bitwise_and(iweight, (2**bits) - 1)
    izeros = torch.bitwise_and(izeros, (2**bits) - 1)

    # Subtract 1 from the izeros tensor (exllama adds 1 during inference)
    # We can remove it if we remove the +1 in the exllama code
    izeros = izeros - 1
    # Pack the qweight and qzeros tensors
    qweight, qzeros = pack_exllama(iweight, izeros, bits)

    return qweight, qzeros


def dequantize_gemm(qweight, qzeros, scales, bits, group_size):
    # Unpack the qweight and qzeros tensors
    iweight, izeros = unpack_awq(qweight, qzeros, bits)
    # Reverse the order of the iweight and izeros tensors
    iweight, izeros = reverse_awq_order(iweight, izeros, bits)

    # overflow checks
    iweight = torch.bitwise_and(iweight, (2**bits) - 1)
    izeros = torch.bitwise_and(izeros, (2**bits) - 1)

    # fp16 weights
    scales = scales.repeat_interleave(group_size, dim=0)
    izeros = izeros.repeat_interleave(group_size, dim=0)
    iweight = (iweight - izeros) * scales

    return iweight
