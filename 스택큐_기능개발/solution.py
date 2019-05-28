import math


def solution(progresses, speeds):
    answer = []
    rest_time = []
    for index, value in enumerate(progresses):
        rest_time.append(math.ceil((100 - value) / speeds[index]))
        print(value)
    print(rest_time)

    all_time = 0
    for time in rest_time:
        if all_time < time:
            answer.append(1)
            all_time = time
        else:
            answer[-1] += 1
    print(all_time)
    return answer


def solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        print(p, s, -((p-100)//s))
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    print(Q)
    return [q[1] for q in Q]


print(solution2([93, 30, 55], [1, 30, 5]))
