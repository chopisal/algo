cash_dic = {}


def get_sum(val, row_index, col_index, triangle):
    if row_index == 0:
        return val

    left = -1
    right = -1
    if col_index - 1 >= 0:
        tmp_key = str(row_index-1)+":"+str(col_index-1)
        if tmp_key in cash_dic:
            left = cash_dic[tmp_key] + val
    if len(triangle[row_index-1]) > col_index:
        right = get_sum(val + triangle[row_index-1][col_index],
                        row_index-1, col_index, triangle)
        cash_dic[str(row_index-1)+":"+str(col_index)] = right - val

    if left > right:
        return left
    else:
        return right


def solution(triangle):
    row_index = len(triangle) - 1
    print(row_index)
    total = 0
    for col_index, tri in enumerate(triangle[-1]):
        tmp_sum = get_sum(tri, row_index, col_index, triangle)
        if total < tmp_sum:
            total = tmp_sum
        # break
    print(cash_dic)
    return total


tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))
