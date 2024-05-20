# 2초 / 256MB

n, k = map(int, input().split())

initial = [str(i) for i in range(1, n + 1)]
flag = [0] * n
answer = []

cnt = 1
idx = 0
while len(answer) < n:
    if cnt == k and flag[idx] == 0:
        answer.append(initial[idx])
        flag[idx] = 1
        cnt = 1

    if not flag[idx]:
        cnt += 1

    idx += 1
    if idx >= n:
        idx = idx % n


result = "<"
for i in range(n):
    if i != n - 1:
        result += answer[i] + ", "
    else:
        result += answer[i] + ">"

print(result)
