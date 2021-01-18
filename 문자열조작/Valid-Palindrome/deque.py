import collections

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    strs = collections.deque()
    for char in s:
        if char.isalnum():  ## isalinum()
            strs.append(char.lower())  ## .lower()

    while len(strs) > 1:  # 문자들을 리스트에서 제거하면서 판단
        if strs.popleft() != strs.pop():
            return False

    return True

print(isPalindrome(s))  #True
