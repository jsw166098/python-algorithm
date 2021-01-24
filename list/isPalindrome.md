# 팰린드롬 연결 리스트

## 리스트 변환

* 팰린드로 여부는 앞뒤로 모두 추출할 수 있는 자료구조 필요
* 리스트의 경우 인덱스를 자유롭게 지정할 수 있다.

~~~
    def isPalindrome1(self, head):
        q = []
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) >1:
            if q.pop(0) != q.pop():
                return False
        return True
~~~

## 데커를 이용한 최적화

* 데크란 이중 연결리스트 이다.
* 동적 배열로 구성된 리스트의 경우 맨 앞 요소를 가져오기에 적합한 자료형이 아니다.
* 리스트에서 첫 번째 자료형을 가져올 경우 모든 값이 한 칸씩 시프팅되며 시간 복잡도는 O(n)이 발생된다. 
* 데크를 사용할 경우 양쪽 모두 O(1) 이 발생된다.

~~~
    def isPalindrome2(self, head):
        q = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:  # while 구문
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
~~~