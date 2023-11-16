class Solution(object):
    def checkInclusion(self, s1, s2):
        # If the length of s2 is less than of s1, s1 cannot be a permutation of s2
        if len(s2) < len(s1):
            return False

        # Initialize dictionaries to store character counts for s1 and the current window in s2
        char_count_s1 = {}
        char_count_s2 = {}

        # Populate char_count_s1 with the counts of characters in s1
        for char in s1:
            char_count_s1[char] = char_count_s1.get(char, 0) + 1

        # Initialize the window indices
        n = len(s1)
        l, r = 0, n - 1

        # Populate char_count_s2 with the counts of characters in the initial window of s2
        for char in s2[l:r]:
            char_count_s2[char] = char_count_s2.get(char, 0) + 1

        # Slide the window through s2 and check for permutations of s1
        while r < len(s2):
            # Update char_count_s2 for the new character in the window
            char_count_s2[s2[r]] = char_count_s2.get(s2[r], 0) + 1

            # Check if the current window's character counts match those of s1
            if char_count_s2 == char_count_s1:
                return True

            # Update char_count_s2 for the character leaving the window
            char_count_s2[s2[l]] -= 1

            # Remove the character from char_count_s2 if its count becomes zero
            if char_count_s2[s2[l]] == 0:
                del char_count_s2[s2[l]]

            # Slide the window to the right
            l += 1
            r += 1

        # No permutation found in s2
        return False
