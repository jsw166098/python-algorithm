# 두 수의 합

## 1. 부루트 포스

def twoSum1(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

## 2. in 사용

def twoSum2(self, nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement)+(i+1)

## 3. 첫 번째 수를 뺀 결과 키 조회

def twoSum3(self, nums, target):
    nums_map = {}

    for i,num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target-num]

## 4. 조회 구조 개선

def twoSum4(self, nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

## 5. 투 포인터 이용

def twoSum5(self, nums, target):
    left, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터 왼쪽으로
        if nums[left] + nums[right] < target:
            left +=1
        # 합이 타겟보다 작으면 왼쪽 포인터 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right

