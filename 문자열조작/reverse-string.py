# 문자열 뒤집기

## 1.투 포인터 사용
def reverseString1(self, s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

## 2.파이썬 다운 방식
def reverseString2(self, s):
    s.reverse


