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
            # Initialize a count list for all 26 letters of the alphabet
            count = [0] * 26
            # Count the frequency of each letter in the string
            for char in string:
                count[ord(char) - ord('a')] += 1
            # Use the count list as a key for the anagrams.
            # Convert the list to a tuple to make it hashable and use it as a dictionary key.
            key = tuple(count)

            # Append the string to the list corresponding to the key in the anagrams dictionary
            anagrams[key].append(string) 

        return list(anagrams.values())