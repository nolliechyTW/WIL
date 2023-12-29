# brute force
class Solution:
    def intToRoman(self, num: int) -> str:
        # in decreasing order so that we can use greedy approach to solve
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numeral = []

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman_numeral.append(romans[i])

        return ''.join(roman_numeral)


# improved - hashtable
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        roman_numeral = []

        for value, symbol in roman_map.items():
            while num >= value:
                num -= value
                roman_numeral.append(symbol)

        return ''.join(roman_numeral)

