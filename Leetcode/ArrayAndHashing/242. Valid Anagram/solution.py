class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable_s = {}
        hashtable_t = {}

        for char in s:
            if char in hashtable_s:
                hashtable_s[char] += 1
            else:
                hashtable_s[char] = 1
        
        for char in t:
            if char in hashtable_t:
                hashtable_t[char] += 1
            else:
                hashtable_t[char] = 1
        
        return hashtable_s == hashtable_t
    
# improve the code above by using get() method of dictionary

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_char_count_dict(string):
            char_count = {}
            for char in string:
                char_count[char] = char_count.get(char, 0) + 1
            return char_count

        return create_char_count_dict(s) == create_char_count_dict(t)
