class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairedCharsCount = 0
        unpaired_chars = set()
        
        for char in s:
            # If the character is unpaired, pair it and add to the count
            if char in unpaired_chars:
                pairedCharsCount += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        # The length of the longest palindrome is twice the number of pairs,
        # plus 1 if there is at least one unpaired character (for the center of the palindrome)
        return pairedCharsCount * 2 + 1 if unpaired_chars else pairedCharsCount * 2