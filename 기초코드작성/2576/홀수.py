sum = 0
min_odd = 101

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        sum += num
        if num < min_odd:
            min_odd = num
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min_odd)