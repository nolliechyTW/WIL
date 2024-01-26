class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by_char = {}

        for value in strs:
            key = ''.join(sorted(value)) # 'cool' --sorted--> ['c', 'l', 'o', 'o'] --join--> 'cloo'
            if key in group_by_char:
                group_by_char[key].append(value)
            else:
                group_by_char[key] = [value]
        # retrieves all the values from the map and turn them into a list of lists
        return list(group_by_char.values())
    
# alternate solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by_char = defaultdict(list)

        for value in strs:
            key = ''.join(sorted(value))  # Sort the string and join back into a string
            group_by_char[key].append(value)

        return list(group_by_char.values())
    