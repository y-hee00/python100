# -*- coding: utf-8 -*-
"""5단계.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gya10fIUiZrDeiq0KiItKGDUbG40D32j

1번
"""

cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)​

"""2번"""

num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)

"""3번"""

a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)

"""4번"""

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

"""5번"""

n = int(input())  # 과목 수
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/max_score *100)  # 새로운 점수 생성
test_avg = sum(new_list)/n
print(test_avg)

"""6번"""

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)

"""7번"""

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')