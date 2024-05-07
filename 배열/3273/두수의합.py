# 1초 / 128MB

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
result = 0

# 알고리즘 = 투포인터

# 배열 오름차순 정렬
nums.sort()

# 두개의 인덱스(left, right) 끝에서부터 시작
left = 0
right = n-1

while left < right:
    if nums[left] + nums[right] > x:
        right -= 1
    elif nums[left] + nums[right] < x:
        left += 1
    else:
        result += 1
        left += 1
        right -= 1
print(result)