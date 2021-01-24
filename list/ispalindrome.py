
# 팰린드롬 연결 리스트

## 리스트 변
def isPalindrome1(self, head):
    q = []
    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

## 데크를 이용한 최적화

    def isPalindrome2(self, head):
        q = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True