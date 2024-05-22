# 512MB, 2초
# 최대 6000000글자까지 입력 가능

import sys

input = sys.stdin.readline

edit_input = input().rstrip()
m = int(input())
conduct = list(input().rstrip() for _ in range(m))

edit = [e for e in edit_input]
temp = []

for c in conduct:
    if c == "L" and edit:
        temp.append(edit.pop())
    elif c == "D" and temp:
        edit.append(temp.pop())
    elif c == "B" and edit:
        edit.pop()
    elif c[0] == "P":
        edit.append(c[2])
print("".join(edit), "".join(temp[::-1]), sep="")
