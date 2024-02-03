# categorized by string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by_char = defaultdict(list)

        for value in strs:
            key = ''.join(sorted(value))  # 'cool' --sorted--> ['c', 'l', 'o', 'o'] --join--> 'cloo'
            group_by_char[key].append(value)
        # retrieves all the values from the map and turn them into a list of lists
        return list(group_by_char.values())
    

# categorized by count (better) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)

            # Append the string to the list corresponding to the key in the anagrams dictionary
            anagrams[key].append(string) 

        return list(anagrams.values())