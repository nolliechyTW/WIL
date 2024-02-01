# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        if not lists:
            return None

        return self.merge_lists(lists, 0, len(lists) - 1)

    def merge_lists(self, lists, start, end):
        # base case of the recursion: when there is only one list 
        if start == end:
            return lists[start]
        
        # divide the lists into two parts and merge them recursively
        mid = (start + end) // 2
        left = self.merge_lists(lists, start, mid)
        right = self.merge_lists(lists, mid + 1, end)

        # conquer the subproblems
        return self.merge_two_lists(left, right)

    def merge_two_lists(self, l1, l2):
        current = dummy = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next



# Assuming ListNode and Solution classes are defined as per your provided code
# Step 1: Create individual linked lists
# For example, let's create three linked lists: [1,4,5], [1,3,4], and [2,6]

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Create linked lists
list1 = create_linked_list([1, 4, 5])
list2 = create_linked_list([1, 3, 4])
list3 = create_linked_list([2, 6])

# Step 2: Instantiate the Solution class
solution = Solution()

# Step 3: Call the mergeKLists method
merged_list_head = solution.mergeKLists([list1, list2, list3])

# The merged_list_head is now the head of the merged linked list


### another solution
### Time Complexity: O(Nlogk), where N is the total number of elements in all the linked lists and k is the number of linked lists.
    # heap initialization takes O(k * log k) time (heap insertion operation takes O(log k) time and it is performed k times).
    # heap pop/push operation takes O(n * log k) time (performed n times).
    # since k log k < n log k, the overall time complexity is O(N log k).
### Space Complexity: O(k), where k is the number of linked lists.
    # The heap will contain at most one node from each of the k lists at any time, making the space complexity for the heap O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        # Initialize a heap with the first node of each list, if not empty
        min_heap = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapq.heapify(min_heap)

        # Dummy node to start the merged list
        head = current = ListNode(None)

        while min_heap:
            val, idx = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next

            # Move to the next node in the chosen list and add it to the heap
            next_node = lists[idx].next
            lists[idx] = next_node
            if next_node:
                heapq.heappush(min_heap, (next_node.val, idx))

        return head.next
