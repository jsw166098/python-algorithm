# 패열 파티션

## 오름차순 풀이
def arrayPairSum1(self, nums):
    nums.sort()
    pair = []
    sum = 0

    for i in nums:
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

## 짝수 번재 값 계산
def arrayPairSum2(self, nums):
    nums.sort()
    sum = 0
    for i, n in enumerate(nums):

        if i % 2 == 0:
            sum += n
    return sum

## 파이썬 다운 방식
def arrayPairSum3(self, nums):
    return sum(sorted(nums)[::2])