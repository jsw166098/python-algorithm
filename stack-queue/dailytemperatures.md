# 일일 온도

## 스택 값 비교

* 자기 보다 작은 것 또는 큰 것 찾는 것 -> 스택 이용
* 인덱스를 스택에 쌓는다.
* 리스트 스택에서 top은 stack[-1]이다.

~~~
def dailyTemperatures(self, T):
    answer = [0] * len(T)  ## 디폴트 0으로 둔다.
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer
~~~