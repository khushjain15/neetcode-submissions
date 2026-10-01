class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = "".join([c.lower() for c in s if c.isalnum()])
        i = 0
        j = len(sNew)-1
        while i < j:
            if sNew[i] != sNew[j]:
                return False
            i += 1
            j -= 1
        
        return True
