class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        ans = ""

        t_dict = {}
        s_dict = {}

        # Initialize the frequency dictionary for the target string t
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        # Initialize pointers for the sliding window
        left = 0
        right = 0

        # Counter to keep track of the characters in t that are present in the current window
        required_chars = len(t)

        while right < s_len:
            # Expand the window to the right
            if s[right] in t_dict:
                s_dict[s[right]] = s_dict.get(s[right], 0) + 1
                if s_dict[s[right]] <= t_dict[s[right]]:
                    required_chars -= 1

            # Contract the window from the left
            while required_chars == 0:
                # Update the answer if the current window is smaller
                if not ans or (right - left + 1) < len(ans):
                    ans = s[left:right + 1]

                # Contract the window by moving the left pointer
                if s[left] in t_dict:
                    s_dict[s[left]] -= 1
                    if s_dict[s[left]] < t_dict[s[left]]:
                        required_chars += 1

                left += 1

            # Move the right pointer to expand the window
            right += 1

        return ans
