def solution(numbers):
    answer = ''
    max_len = len(str(max(numbers)))

    tmp_array = []

    for index, val in enumerate(numbers):
        print(index, val)
        t = str(val).ljust(max_len, str(val)[0])
        tmp_array.append((index, t))

    tmp_array = sorted(tmp_array, key=lambda x: int(x[1]), reverse=True)

    for val in tmp_array:
        answer += str(numbers[val[0]])
    if int(answer) == 0:
        return "0"
    print(tmp_array)
    print(answer)
    return answer


# ar = [40, 403]
# ar = [40, 405]
# ar = [40, 404]
# ar = [12, 121]
# ar = [25, 22, 223, 0]
# ar = [21,212]
# ar = [41, 415]
# ar = [5, 546]
ar1 = [0, 0, 0, 1000]
ar2 = [0, 0, 1000, 0]
ar3 = [1000, 0, 0, 0]
# ar = [2, 22]
# ar = [70, 0, 0, 0]
# ar = [0,0,0,0]
# ar = [0, 0, 0, 1000]
# ar = [12, 1213]
solution(ar1)
solution(ar2)
solution(ar3)
