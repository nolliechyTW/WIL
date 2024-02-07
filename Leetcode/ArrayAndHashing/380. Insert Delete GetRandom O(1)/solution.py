class RandomizedSet:

    def __init__(self):
        self.myMap = defaultdict(set)
        self.myList = []

    def insert(self, val: int) -> bool:
        if val in self.myMap:
            return False
        self.myMap[val] = len(self.myList) # key: value, value: index of the value in the list
        self.myList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.myMap:
            index = self.myMap[val]
            lastValue = self.myList[-1]

            # Swap the last element with the element to delete
            self.myList[index], self.myList[-1] = self.myList[-1], self.myList[index]

            # Update the 'myMap' for the new index of the last element
            self.myMap[lastValue] = index
            
            # Remove the last element from 'myList'
            self.myList.pop()

            # Delete the element from 'myMap'
            del self.myMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.myList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()