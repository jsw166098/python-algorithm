# 문자열 뒤집기

* 두 포인터 사용
* 

---

## 두 포인터 사용

* 두 포인터를 통해 범위를 좁혀가며 스왑시킨다.

~~~
    def reverseString1(self, s):
        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

~~~

## 파이썬 다운 방식

* 파이썬의 기본 기능을 잘 활용한 방식

~~~
def reverseString2(self, s):
    s.reverse
~~~

* 추가저으로 다음과 같이 사용 가능하다.

~~~
s = s[::-1]  ## 리트코드에서는 불가능
s[:] = s[::-1]
~~~

---

## 문법

#### 여러개 변수 동시 초기화

~~~
left, right = 1, 2
~~~

### 1. [::-1]

* 슬라이싱은 리스트와 문자열 모두에서 사용할 수 있다.

### 2. reverse

* 리스트 요소들을 뒤 바꿔준다.
* 리스트에서만 사용가능하다.

### 3. 리스트와 sort 함수

* 숫자로 구성
* 오름차순으로 위치
~~~
a = [1, 10, 5, 7, 6]
a.sort()
a  ## [1,5,6,7,10]
~~~

* 문자로 구성
* 아스키 코드값 순으로 정렬(첫문자의)
~~~
str = ['aa', 'cc', 'bb']
str.sort()
str  ## ['aa', 'cc', 'bb']

s = ['2A', '1B', '4C', '1A']
s  ## ['1A', '1B', '2A', '4C']
~~~

* key 옵션 사용 -> 기준 설정
* 문자열 길이를 기준
~~~
m = '나는 파이썬을 잘하고 싶다'
m = m.split()
m.sort(key=len)
m  ## ['파이썬을', '잘하고', '나는', '싶다']
~~~

* sort vs sorted
* sort -> 값 자체를 변환
* sorted-> 값 자체를 변환하시키 않은(바뀐 값을 반환하기만 한다.)

