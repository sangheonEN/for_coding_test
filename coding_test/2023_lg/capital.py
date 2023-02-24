"""
전형적인 다익스트라 알고리즘.
노드와 간선으로 이루어진 graph 구조가 있다.
노드간 연결은 양방향이다.

입력
1. n: node의 갯수

2. k: 수도권의 거리 기준

2. kapital node 정보: [1, 2]

3. graph 정보: [[n1, n2, distance(1, 2)],
            [n2, n3, distance(2, 3)],
            [n3, n4, distance(3, 4)],
            ...]

우리는 수도권을 찾아야한다.
수도권의 정의는 수도에서 주어진 k 거리 이하에 위치한 node들을 수도권이라 칭한다.
수도권에 해당하는 node를 오름차순으로 출력하시오.

제약조건: kapital은 수도권이 아니다.

출력: [수도권 노드 번호]

"""