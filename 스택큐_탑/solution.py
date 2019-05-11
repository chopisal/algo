
def solution(heights):
    answer = []
    print(heights)
    for index, value in enumerate(heights):
        print(index, value)
        val = 0
        curIndex = index
        curVal = value
        while curIndex > 0:
            if heights[curIndex-1] > curVal:
                val = curIndex
                break
            curIndex -= 1
        answer.append(val)
        
    return answer

arr = [6,9,5,7,4]

print(solution(arr))