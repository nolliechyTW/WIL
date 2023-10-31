class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by_char = {}

        for value in strs:
            key = ''.join(sorted(value))
            if key in group_by_char:
                group_by_char[key].append(value)
            else:
                group_by_char[key] = [value]
        # retrieves all the values from the map and turn them into a list of lists
        return list(group_by_char.values())
