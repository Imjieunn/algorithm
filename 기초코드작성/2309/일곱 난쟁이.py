# nanjjangs = []
# sum = 0

# for i in range(9):
#     nanjjang = int(input())
#     nanjjangs.append(nanjjang)
#     sum += nanjjang

# diff = sum - 100

# for i in range(8):
#     found = False
#     for j in range(i+1, 9):
#         if nanjjangs[i] + nanjjangs[j] == diff:
#             a = nanjjangs[i]
#             b = nanjjangs[j]
#             nanjjangs.remove(a)
#             nanjjangs.remove(b)
#             found = True
#             break
#     if found:
#         break

# nanjjangs.sort()
# print(*nanjjangs,sep='\n')

from itertools import combinations

nanjjangs =[]
for i in range(9):
    nanjjangs.append(int(input()))

for i in (combinations(nanjjangs,7)):
    if sum(i) == 100:
        print(*sorted(i),sep='\n')
        break