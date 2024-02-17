class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t and char_t not in mapping_t_to_s:
                mapping_s_to_t[char_s] = char_t
                mapping_t_to_s[char_t] = char_s
            elif mapping_s_to_t.get(char_s) != char_t or mapping_t_to_s.get(char_t) != char_s:
                return False
        return True
# note: the use of mapping_to_t[char_s] in the condition would 
# indeed raise a KeyError if char_s is not already a key in the dictionary mapping_to_t.



# to prevent key error, we can use the get method of dictionary
class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        mapping_s_to_t = defaultdict(str)
        mapping_t_to_s = defaultdict(str)
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping_s_to_t and char_t not in mapping_t_to_s:
                mapping_s_to_t[char_s] = char_t
                mapping_t_to_s[char_t] = char_s
            elif mapping_s_to_t[char_s] != char_t or mapping_t_to_s[char_t] != char_s:
                return False
        return True
    