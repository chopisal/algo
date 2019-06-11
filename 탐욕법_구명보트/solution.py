def solution(people, limit):
    w_dic = {}
    for val in people:
        w_dic[val] = 0
    for index, p_weight in enumerate(people):
        rest = limit - p_weight
        is_pair = False
        pair_idx = -1
        max_val = max(people)
        if rest > 0 and rest <= max_val:
            for y, other in enumerate(people[index+1:]):
                min_diff = 240
                if other <= rest and min_diff > rest - other:
                    min_diff = rest - other
                    is_pair = True
                    pair_idx = y + index + 1
                    if min_diff == 0:
                        break
        if is_pair:
            del people[pair_idx]

    return len(people)


def sol2(people, limit):
    people.sort()
    light = 0
    heavy = len(people) - 1
    pair = 0
    while(light < heavy):
        if people[light] + people[heavy] <= limit:
            pair += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1
    return len(people) - pair


# => 5 가 나와야합니다!
print(sol2([60, 90, 10, 20, 80, 30, 40,  50, 70], 100))
