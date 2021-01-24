# 리스트로 변환

## 제약 조건 처리

* 영어, 숫자만 다룬다.
* 불 결과만 얻으면된다. -> 리스트 내 요소를 삭제하든 말든 자유!!

~~~
s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    strs = []
    for char in s:
        if char.isalnum():  ## isalinum()
            strs.append(char.lower())  ## .lower()

    while len(strs) > 1:  # 문자들을 리스트에서 제거하면서 판단
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindrome(s))  #True
~~~

## 문법

#### isalnum

* 영어, 한글, 숫자 판단 
~~~
isalnum(dd)  ## True
~~~

#### lower()

* 소문자로 바꿈
* 한글, 숫자에 사용하면 그대로

~~~
a = 'A'

a.lower()  ##'a'
a  ## 'A'
~~~