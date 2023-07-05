n = int(input())

As = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())


def find_max(ans, Nums, plus, minus, multi, div):
    if len(Nums) > 0:
        plusC = -1000000000
        minusC = -1000000000
        multiC = -1000000000
        divC = -1000000000
        if plus > 0:
            plusC = find_max(ans + Nums[0], Nums[1:], plus - 1, minus, multi, div)
        if minus > 0:
            minusC = find_max(ans - Nums[0], Nums[1:], plus, minus - 1, multi, div)
        if multi > 0:
            multiC = find_max(ans * Nums[0], Nums[1:], plus, minus, multi - 1, div)
        if div > 0:
            if ans >= 0:
                divC = find_max(ans // Nums[0], Nums[1:], plus, minus, multi, div - 1)
            else:
                divC = find_max(
                    -(-ans // Nums[0]), Nums[1:], plus, minus, multi, div - 1
                )

        return max(plusC, minusC, multiC, divC)

    else:
        return ans


def find_min(ans, Nums, plus, minus, multi, div):
    if len(Nums) > 0:
        plusC = 1000000000
        minusC = 1000000000
        multiC = 1000000000
        divC = 1000000000
        if plus > 0:
            plusC = find_min(ans + Nums[0], Nums[1:], plus - 1, minus, multi, div)
        if minus > 0:
            minusC = find_min(ans - Nums[0], Nums[1:], plus, minus - 1, multi, div)
        if multi > 0:
            multiC = find_min(ans * Nums[0], Nums[1:], plus, minus, multi - 1, div)
        if div > 0:
            if ans >= 0:
                divC = find_min(ans // Nums[0], Nums[1:], plus, minus, multi, div - 1)
            else:
                divC = find_min(
                    -(-ans // Nums[0]), Nums[1:], plus, minus, multi, div - 1
                )

        return min(plusC, minusC, multiC, divC)

    else:
        return ans


print(find_max(As[0], As[1:], plus, minus, multi, div))
print(find_min(As[0], As[1:], plus, minus, multi, div))
