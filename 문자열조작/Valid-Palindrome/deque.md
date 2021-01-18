# 데크 자료형 이용

## 데크 사용

* 리스트 사용대신 데크를 사용하면 속도가 더 높아진다.
* 리스트의 pop(0)은 O(n)인 반면 데크의 popleft()는 O(1)이기 때문이다.

~~~
import collections

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    strs = collections.deque()
    for char in s:
        if char.isalnum():  ## isalinum()
            strs.append(char.lower())  ## .lower()

    while len(strs) > 1:  # 문자들을 리스트에서 제거하면서 판단
        if strs.popleft() != strs.pop():
            return False

    return True

print(isPalindrome(s))  #True

~~~

## 문법

#### popleft()

* 데크 함수
