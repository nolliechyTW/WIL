class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """O(n) in Time, O(1) in Space"""
        seen = set()
        left = 0 
        ans = 0 

        # winodw sliding 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1)
        return ans