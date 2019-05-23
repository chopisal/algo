import bisect


def solution(budgets, M):
    sorted_budgets = sorted(budgets)
    sum = 0
    for val in sorted_budgets:
        sum += val
    print("request budgets sum =>", sum, "  budget:", M)
    if M > sum:
        return sorted_budgets[len(budgets) - 1]
    print(sorted(budgets))

    average = M / len(budgets)
    pos = bisect.bisect(sorted_budgets, average)
    print("average", average, "  pos", pos)
    print(sorted_budgets)
    if pos == 0:
        return int(average)

    remain = 0
    for budget in sorted_budgets[0:pos]:
        remain += average - budget

    plus_budget = 0
    over_budgets = sorted_budgets[pos:]

    for index, budget in enumerate(over_budgets):
        need_budget = (budget - average) * (len(over_budgets) - index)

        if remain > need_budget:
            remain = remain - need_budget
            plus_budget = budget - average
            average += plus_budget
            # print("over budget ", budget,  "  need_budget=",
            #       need_budget, "  remain=", remain, "   average=", average)
        else:
            plus_budget = remain / (len(over_budgets) - index)
            average += plus_budget
            # print("2over budget ", budget,  "  need_budget=",
            #       need_budget, "  remain=", remain, "   average=", average)
            break

    # print("average =", average, "  plus_budget =", plus_budget)
    # print("answer=", int(plus_budget + average))

    print("end")
    return int(average)


def solution2(budgets, M):
    lim = max(budgets)

    while True:
        if sum(budgets) < M:
            answer = max(budgets)
            break

        budgets = list(map(lambda x: x if x <= lim else lim, budgets))
        lim = lim-1

    return answer


ans = solution([120, 110, 140, 150, 133], 639)
print(ans)
