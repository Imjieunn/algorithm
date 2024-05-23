k = int(input())
stack = []

for i in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

result = 0
for num in stack:
    result += num

print(result)
