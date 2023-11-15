# key : replace the characers that are less frequent
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencyMap = {}
        res = 0

        left = 0 
        for right in range(len(s)):
            # Update the frequency of the current character
            frequencyMap[s[right]] = frequencyMap.get(s[right], 0) + 1
            
            # while windowSize - maxFrequency > k, we stop expanding the window 
            while (right - left + 1) - max(frequencyMap.values()) > k:
                frequencyMap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res