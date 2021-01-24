# 큐를 이용한 스택 구현

* 큐의 연산: append, popleft
* 큐에 push한 후 재 정렬 시키면 popleft 하면서 스택 구조 형성

~~~
class MyStack(object):

    def __init__(self):
        # 데크로 선언
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
~~~