import bisect


def solution(budgets, M):
    sorted_budgets = sorted(budgets)
    sum = 0
    for val in sorted_budgets:
        sum += val
    print("sum =>", sum, M)
    if M > sum:
        return sorted_budgets[len(budgets) - 1]
    # print(sorted(budgets))

    average = M / len(budgets)
    pos = bisect.bisect(sorted_budgets, average)
    print("average", average, "  pos", pos)
    print(sorted_budgets)
    if pos == 0:
        return average

    remain = 0
    for budget in sorted_budgets[0:pos]:
        remain += average - budget

    up_remain = 0
    for budget in sorted_budgets[pos:]:
        up_remain += budget - average

    sum_bud = int(remain / (len(budgets) - pos))

    print("average =", remain, "  up_remain =", up_remain)
    print("--- ", up_remain - remain)
    add_bug = up_remain - remain

    for i in range(len(budgets)-1, pos-1, -1):
        diff = sorted_budgets[i] - sorted_budgets[i-1]
        add_bug = add_bug - diff
        print()
    print("end")
    return sum_bud + average


ans = solution([120, 110, 140, 150, 133], 641)
print(ans)
