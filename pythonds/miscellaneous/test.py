import pdb

from collections import deque


def isPalindrome(s):
    s = [x.lower() for x in s if x.isalpha()]
    dq = deque(s)
    print(dq)
    # pdb.set_trace()
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
    return True
        

if __name__=="__main__":
    print(isPalindrome("0P"))