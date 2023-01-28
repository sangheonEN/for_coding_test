"""
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

입출력 예
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
"""


s0 = "()()"
s1 = "(())()"
s2 = ")()("
s3 = "(()("


# 문자열을 처음부터 순회하면서 ( 만나면 queue에 넣고 ) 만나면 queue에서 빼고
# queue에 리스트가 있을때만 pop 없는데 ")" 이면, 닫을 수가 없기 때문에 False
# queue가 빈리스트가 되면 True, 비지 않으면 False

from collections import deque


def solution(s):
    queue = []

    for _ in s:
        if _ == "(":
            queue.append(_)
        elif _ == ")" and queue:
            queue.pop()
        else:
            return False

    return False if queue else True


solution(s1)

