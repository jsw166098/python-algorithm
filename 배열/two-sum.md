# 두 수의 합

~~~
Input: nums = [2,7,11,15], target = 9

Output: [0,1]
~~~

* 두 수의 합을 비교한다.
* 인덱스를 구한다.

## 1. 부루트 포스

* 부르트 포스란 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 방식이다ㅏ.
* 비효율적인 방법으로 최적화된 방법을 사용해야 한다.
* O(n^2) 시간 복잡도를 가진다.

~~~
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
~~~

## 2. in 사용

* 타깃에서 첫 번째 값을 뺀 값을 탐색하는 문제로 변경한다.
* in의 경우도 O(n) 시간 복잡도를 가져 총 O(n^2) 복잡도를 가진다.
* 부루트 포스와 같은 복잡도이지만 상수항 차이가 나기 때문에 더 빠르다.

~~~
def twoSum2(self, nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement)+(i+1)
~~~

## 3. 첫 번째 수를 뺀 결과 키 조회

* 딕셔너리 이용
* 딕셔너리에서 키에 대한 값 조회시 상수 시간 복잡도를 가지기 때문에 인덱스 관련 문제는 딕셔너리로 변환한다.

~~~
def twoSum3( nums, target):
    nums_map = {}

    # 딕셔너리로 변경 
    for i,num in enumerate(nums):
        nums_map[num] = i

    # 첫 번째 수를 뺀 결과 사용 -> 그렇지 않을 시 2중 for 문을 사용해야 할 수도 있다.
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target-num]
~~~

## 4. 조회 구조 개선

~~~
def twoSum4(self, nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i
~~~

## 5. 투 포인터 이용

* 투 포인터란 왼쪽 포인터, 오른쪽 포인터의 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로 그 반대이면 왼쪽 포인터를 오른쪽으로 이동하여 값을 조정하는 방식
* 다음의 코드는 정렬이 되어 있어야 한다. 
* 만약 sort 함수를 사용할 경우 인덱스 값이 변경되기 때문에 주의해야 한다. 

~~~
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
~~~