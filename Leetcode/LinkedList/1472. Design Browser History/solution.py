# method 2: Using List
class BrowserHistory:
    def __init__(self, homepage: str):
        # Initialize two stacks: '_history' to keep track of the URLs visited before the current URL,
        # and '_future' to keep track of the URLs visited after the current URL when going back.
        self._history, self._future = [], []
        # Initialize the current page to 'homepage'. This is the starting point of the browser history.
        self._current = homepage

    def visit(self, url: str) -> None:
        """
        Navigates to a new URL.
        
        The current URL is pushed onto the '_history' stack, and the new URL becomes the current page.
        The '_future' stack is cleared because a new URL visit breaks the forward navigation chain.
        """
        self._history.append(self._current)  # Save the current URL to history before navigating away.
        self._current = url  # Update the current URL to the new one.
        self._future = []  # Clear the future since we're starting a new navigation path.

    def back(self, steps: int) -> str:
        """
        Moves back in the browser history by a specified number of steps.
            
        For each step back, the current URL is moved to the '_future' stack, and the last URL from
        the '_history' stack becomes the current URL.
        """
        while steps > 0 and self._history:
            self._future.append(self._current)  # Save the current URL to the future before going back.
            self._current = self._history.pop()  # Set the current URL to the last visited URL from the history.
            steps -= 1
        return self._current

    def forward(self, steps: int) -> str:
        """
        Moves forward in the browser history by a specified number of steps, if available.
            
        For each step forward, the current URL is moved to the '_history' stack, and the last URL from
        the '_future' stack becomes the current URL.
        """
        while steps > 0 and self._future:
            self._history.append(self._current)  # Save the current URL to the history before going forward.
            self._current = self._future.pop()  # Set the current URL to the next URL from the future.
            steps -= 1
        return self._current



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
