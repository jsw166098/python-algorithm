# 일일 온도

## 스택 값 비교
def dailyTemperatures(self, T):
    answer = [0] * len(T)  ## 디폴트 0으로 둔다.
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer