# 1초, 256MB
# 1 ≤ L ≤ 1,000,000
import sys

input = sys.stdin.readline

n = int(input())


# 방법2. 연결리스트 풀이
def sol2(pw):
    pwd = []
    sub = []
    for i in pw:
        if i == "<":
            if pwd:
                sub.append(pwd.pop())
        elif i == ">":
            if sub:
                pwd.append(sub.pop())
        elif i == "-":
            if pwd:
                pwd.pop()
        else:
            pwd.append(i)

    print("".join(pwd), "".join(sub[::-1]), sep="")


for _ in range(n):
    pw = input().rstrip()
    sol2(pw)
