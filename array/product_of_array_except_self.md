# 자신을 제외한 배열의 곱

~~~
Input:  [1,2,3,4]

Output: [24,12,8,6]
~~~

## 내 풀이

~~~
    def productExceptSelf(self, nums):
        results = []
        mult = 1

        for i in nums:
            for j in nums:
                if i == j:
                    continue
                mult *= j
            results.append(mult)
            mult = 1
        return results
~~~

## 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

* 왼족, 오른쪽 나누다.
* 리스트 형태로 곱한다.
* range(x,y,z)의 z는 증감을 나타낸다.

~~~
    def productExceptSelf(self, nums):
        out = []
        p = 1
        
        for i in  range(len(nums)):
            out.append(p)
            p = p*nums[i]
        
        p = 1
        
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i]*p
            p = p * nums[i]
        return out
~~~