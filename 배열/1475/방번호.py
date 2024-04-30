n = input()
result = 0

num_dict = {'0':0, '1':0, '2':0 , '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for i in range(len(n)):
    num_dict[n[i]] += 1

max_num = max(num_dict.values())

for k, v in num_dict.items():
    if k == '6' or k == '9':
        max_num = num_dict['6'] + num_dict['9']
        if max_num % 2 == 0:
            if max_num//2 > result:
                result = max_num//2
        else:
            if max_num//2 + 1 > result:
                result = max_num//2 + 1

    else:
        if v > result:
            result = v
print(result)

# 반례) 66699 : 결과값 3나와야 하는데 2로 나옴