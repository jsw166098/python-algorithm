# 유효한 괄호

* 매핑 테이블을 먼저 만든 후 테이블에 존재하지 않으면 무조건 푸시하고 팝했을 때 결과가 일치하지 않으면 False를 리턴 하도록 구현한다.

## 스택 일치 여부 판별

* 스택을 리스트를 활용하여 구현

~~~
    def isValid(self, s):
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        # 스택이 비워있는 경우에 대한 예외 처리 추가
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0
~~~