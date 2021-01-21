# 자신을 제외한 배열의 곱

## 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

def productExceptSelf(self, nums):
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1

    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out