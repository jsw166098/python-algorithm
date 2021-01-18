# 리스트로 변환

## 제약 조건 처리

* 영어, 숫자만 다룬다.
 
~~~
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())
~~~
