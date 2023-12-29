class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of strings for each row
        rows = [''] * numRows
        idx, step = 0, 1

        for char in s:
            rows[idx] += char
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step

        # Combine the rows to get the final string
        return ''.join(rows)
            