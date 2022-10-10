# 1D2S#10S
# 1D#2S*3S

# S^1, D^2, T^3
# *: 해당점수와 이전점수 각 2배, 첫번째 기회에서 나올 수 있음, 이 경우 첫번째만 2배, 중첩 가능, 아차상과 중첩 가능
# #: 해당점수는 마이너스
# 총 점수 반환 함수 작성

def solution(dartResult):

    score_arr = []

    for idx, i in enumerate(dartResult, 1):

        if i == 'D':
            score_arr[-1] **= 2
        elif i == 'S':
            score_arr[-1] **= 1
        elif i == 'T':
            score_arr[-1] **= 3
        elif i == '*':
            score_arr[-1] *= 2
            if len(score_arr) > 1:
                score_arr[-2] *= 2

        elif i == '#':
            score_arr[-1] *= -1

        else:
            if i == '1' and dartResult[idx] == '0':
                score_arr.append(10)
            elif i == '0':
                if dartResult[idx-1] == '1':
                    pass
            else:
                score_arr.append(int(i))

    return score_arr

total_score_arr = solution("1D2S#10S")

total_score = sum(total_score_arr)

print(total_score)



"""

for i in range(len(dartResult)):
    if dartResult[i] == '1':
        if dartResult[i + 1] == '0':

            if dartResult[i] == "D":
                total_score += int(dartResult[i - 1]) ** 2

            if dartResult[i] == "S":
                total_score += int(dartResult[i - 1]) ** 1

            if dartResult[i] == "T":
                total_score += int(dartResult[i - 1]) ** 3

            if dartResult[i] == "*":
                if i < 3:
                    total_score += int(dartResult[i - 2]) * 2
                else:
                    total_score += int(dartResult[i - 4]) * 2 + int(dartResult[i - 2]) * 2

            if dartResult[i] == "#":
                total_score += int(dartResult[i - 2]) * -1

        else:

            if dartResult[i] == "D":
                total_score += int(dartResult[i - 1]) ** 2

            if dartResult[i] == "S":
                total_score += int(dartResult[i - 1]) ** 1

            if dartResult[i] == "T":
                total_score += int(dartResult[i - 1]) ** 3

            if dartResult[i] == "*":
                if i < 3:
                    total_score += int(dartResult[i - 2]) * 2
                else:
                    total_score += int(dartResult[i - 4]) * 2 + int(dartResult[i - 2]) * 2

            if dartResult[i] == "#":
                total_score += int(dartResult[i - 2]) * -1 
                
"""