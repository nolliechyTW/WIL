class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # if not alphanumeric, move forward
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # if characters are different, return False
            if s[left].lower() != s[right].lower():
                return False
            # update pointer 
            left += 1
            right -= 1

        return True
