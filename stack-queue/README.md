# 스택, 큐

## 스택

* LIFO(Last-In-First-Out)

### 스택의 주요 연산

* push(): 요소를 컬렉션에 추가한다.
* pop(): 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.
* 리스트로 스택을 구현할 경우 push -> append(), pop -> poop()

### 연결 리스틀를 이용한 스택 ADT 구현

~~~
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.last = None
        
    def push(self, item):
        self.last = Node(item, self.last)
        
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for  _ in range(5):
    print(stack.pop())
~~~

~~~
1. stack = Stack()
self.last = None

2. stack = push(1)
self.last = Node(1, None)
1(last) -> None

3. stack = push(2)
self.last = Node(2, Node1)
2(last) -> 1 -> None

...

6. stack = push(5)
self.last = Node(5, Node4)
5(last) -> 4 -> 3 -> 2 -> 1 -> None
~~~

---

## 큐

* FIFO(First-In-Fist-Out)
* 큐 자체를 사용하는 것은 상대적으로 적다.
* 데크, 우선순위 큐, 너비 우선 탐색, 캐스 등을 구혀할 때 많이 쓰인다.


---

## 리스트

* 파이썬에선 스택, 큐에 대한 모든 연산을 지원한다.
* 하지만 동적 배열이기 때문에 큐의 연산을 처리하기에 효율적이지 않다.
* 큐 연산의 경우 데크(이중 연결 리스트)를 사용한다.

