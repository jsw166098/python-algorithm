# 배열 파티션

~~~
Input: nums = [1,4,3,2]

Output: 4
~~~

## 오름차순 풀이 

* min() 값이 커야한다.
* 정렬했을 때 가장 큰 값 즉 가장 끝에 있는 값은 나올 수 없다. 따라서 그 보다 작지만 가장 큰 값을 꺼내면 좋을 것이다.
* 앞에서 부터 차례대로 파티션을 나눠 min을 적용하여 값을 꺼낸다. 

~~~
    def arrayPairSum(self, nums):
        nums.sort()
        pair = []
        sum = 0
        
        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum
~~~

## 짝수 번재 값 계산

* 정렬했을 경우 짝수 번째 값이 크기 때문에 그 값만 가져오는 것을 알 수 있다.

~~~
def arrayPairSum2(self, nums):
    nums.sort()
    sum = 0
    for i, n in enumerate(nums):

        if i % 2 == 0:
            sum += n
    return sum
~~~

## 파이썬 다운 방식

* 슬라이싱 활용

~~~
def arrayPairSum3(self, nums):
    return sum(sorted(nums)[::2])
~~~

