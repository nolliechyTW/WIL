class Solution:
    def partitionString(self, s: str) -> int:
        temp = set()
        ans = 1

        for char in s:
            if char in temp:
                ans += 1
                temp = set()
            temp.add(char)

        return ans