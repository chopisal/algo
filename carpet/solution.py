def solution(brown, red):
    answer = []
    redHeight = 1
    while 1:
        garo = (brown - redHeight*2) / 2
        redWidth = garo - 2
        if redWidth * redHeight == red:
            return [int(garo), redHeight+2]
        else:
            redHeight = redHeight + 1

    return answer


print(solution(24, 24))
