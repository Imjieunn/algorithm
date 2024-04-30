num_list = []
sum = 0

for i in range(5):
    num = int(input())
    sum += num
    num_list.append(num)

print(int(sum/5))
print(sorted(num_list)[2])
