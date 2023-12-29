# brute force
class Solution:
    def reverse(self, x: int) -> int:
        # Convert the integer to a string and reverse it
        reversed_str = str(abs(x))[::-1]

        # Convert back to integer and apply the sign
        reversed_int = int(reversed_str) if x >= 0 else -int(reversed_str)

        # Handle 32-bit integer overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int

