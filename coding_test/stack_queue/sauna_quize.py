# 사우나에 사람이 차례로 앉아 있는데 각 사람들은 인내심을 가지고 있다,
# 1분이 지날때 마다 인내심이 줄어들고 음수가 되었을 때 사우나를 나가고 싶어한다.
# 그런데 맨 앞에 위치한 사람이 양수로 나가지 않게 되면,
# 자존심 때문에 버티다가 맨 앞의 사람이 음수일때 같이 나간다.
# 모든 사람이 나갈때 까지 걸린 시간을 return해라!
# 1분당 인내심이 줄어드는 량은 10이다.

from collections import deque


def solutions(p):

    total_time = 0

    while len(p) > 0:
        # 시간 카운트!
        time = p[0] // 10 + 1

        # 시간 지남에 따라 인내심 최신화
        p = deque([i-time*10 for i in p])

        # 인내심 떨어진 애들 내보내기 (queue 구현으로!)
        while len(p) != 0 and p[0] < 0:
            p.popleft()

        # 바람 들어오는 제약조건
        if len(p) != 0 and p[0] > 0:
            p[0] += 20

        # 최종 시간 더하기
        total_time += time

    return total_time


if __name__ == "__main__":
    p = [25, 5, 20, 45, 15, 55]
    times = solutions(p)

    print(times)
