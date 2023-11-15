class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq, window_size, matched = {}, len(s1), 0

        if len(s1) > len(s2):
            return False

        # Initialize the character frequency dictionary for s1
        for char in s1:
            char_freq[char] = char_freq.get(char, 0) + 1

        unique_chars_in_s1 = len(char_freq)

        # Iterate through s2
        for i in range(len(s2)):
            # Update frequency for the current character in the sliding window
            if s2[i] in char_freq:
                char_freq[s2[i]] -= 1
                if char_freq[s2[i]] == 0:
                    matched += 1

            # Check if the window size is reached 
            #  and update frequency for the character going out of the window
            if i >= window_size:
                left_char = s2[i - window_size]
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1

            # Check if all unique characters in s1 are matched in the current window
            if matched == unique_chars_in_s1:
                return True

        # If no match is found
        return False
