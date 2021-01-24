# 스택을 이용한 큐 구현

* 두개의 스택을 사용한다.
* 하나의 스택을 사용할 경우 다음과 같이 구현되는데 이는 무한 루프를 의미한다.

~~~
        for _ in range(len(self.s)-1):
            self.s.append(self.s.pop())
~~~

~~~
class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x) 

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []
~~~