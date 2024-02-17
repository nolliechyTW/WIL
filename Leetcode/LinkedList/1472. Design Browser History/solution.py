# method 1: Using Linked List
class ListNode:
    def __init__(self, val, pre=None, next=None):
        self.val = val 
        self.pre = pre
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)  # Set the current page's next to the new page and update the new page's previous to current page
        self.curr = self.curr.next  # Move to the new page

    def back(self, steps: int) -> str:
        while self.curr.pre and steps > 0:  # While there's a previous page and steps remain
            self.curr = self.curr.pre  # Move back
            steps -= 1  # Decrement steps
        return self.curr.val  # Return the current page's URL

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:  # While there's a next page and steps remain
            self.curr = self.curr.next  # Move forward
            steps -= 1  # Decrement steps (Corrected)
        return self.curr.val  # Return the current page's URL
