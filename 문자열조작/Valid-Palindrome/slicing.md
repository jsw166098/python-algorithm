# 슬라이시 사용

## 슬라이싱

* [::-1 ] 이용하여 뒤집을 수 있다.
* lower() 함수는 한번에 소문자로 바꿀 수 있다.

~~~
import re

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(isPalindrome(s))  #True
~~~

