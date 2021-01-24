# 세 수의 합

~~~
입력
nums = [-1, 0, 1, 2, -1, -4]

출력
[
    [-1, 0, 1],
    [-1, -1, 2]
]
~~~

## 부르트 포스로 계산

* sort 로 정렬시켜준다.
* 중복되는 부분을 없애준다. 

~~~
def threeSum1(self, nums)
    results = []
    nums.sort()
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j> i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))
~~~

## 투 포인터로 합 계산

1. 정렬
2. for 문을 통해 끝의 2번째 까지 접근
3. 중복 제거
4. 투 포인터 이용
5. 합 계산
6. 합 계산 결과를 통해 투 포인터 이동

~~~
def threeSum2(self, nums):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
         if i >0 and nums[i] == nums[i-1]:
             continue
         left, right = i+1, len(nums) -1
         while left < right:
             sum = nums[i] + nums[left] + nums[right]

             ## sum을 통해서 투 포인터 이동!!
             if sum < 0:
                 left += 1
             elif sum > 0:
                 right += 1 
             else:
                 
                 results.append((nums[i], nums[left], nums[right]))
                 while left < right and nums[left] == nums[left+1]:
                     left += 1
                 
                 while left < right and nums[right] == nums[right-1]:
                     right -= 1
                 
                 left += 1
                 right -= 1
~~~

## 문법 

### 투 포인턴

* 시작점과 끝점 도는 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제 풀이 전략
* 배열을 정렬시킨 후 범위를 좁혀나간다. 