n, r, c = map(int, input().split())


def div_con(r, c, n):
    if n == 0:
        return 0
    r_, c_ = r, c
    if c - n // 2 >= 0:
        c_ = c - n // 2
    if r - n // 2 >= 0:
        r_ = r - n // 2
    if r < n // 2:
        if c < n // 2:  # 1사분면
            return div_con(r_, c_, n // 2)
        else:  # 2사분면
            return div_con(r_, c_, n // 2) + (n // 2) ** 2
    else:
        if c < n // 2:  # 3사분면
            tmp = div_con(r_, c_, n // 2) + (n // 2) ** 2 * 2
            return tmp
        else:  # 4사분면
            return div_con(r_, c_, n // 2) + (n // 2) ** 2 * 3


print(div_con(r, c, 2**n))
