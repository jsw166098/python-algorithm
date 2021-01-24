# 유효한 괄호

## 스택 일치 여부 판별

def isValid(self, s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 스택이 비워있는 경우에 대한 예외 처리 추가
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0