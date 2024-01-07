class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create a trie to store the words for efficient search
        WORD_KEY = '*' # mark the end of the word in the trie
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
            '''
            Let's say words = ["cat", "cap"]. Here's how the trie will be built:

            Start with "cat":

            trie is {}.
            Add 'c': trie = {'c': {}}.
            Add 'a' under 'c': trie = {'c': {'a': {}}}.
            Add 't' under 'a': trie = {'c': {'a': {'t': {}}}}.
            Mark the end of "cat": trie = {'c': {'a': {'t': {'*': 'cat'}}}}.
            Next, add "cap":

            Start from 'c': trie = {'c': {'a': {'t': {'*': 'cat'}}}}.
            'a' is already there under 'c'.
            Add 'p' under 'a': trie = {'c': {'a': {'t': {'*': 'cat'}, 'p': {}}}}.
            Mark the end of "cap": trie = {'c': {'a': {'t': {'*': 'cat'}, 'p': {'*': 'cap'}}}}.
            '''      
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            # It reads the letter in the current cell of the board  
            # and then accesses the corresponding child node in the trie
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited to avoid revisiting the same cell
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
    
    '''
        Imagine a 2x2 board:
        [["c", "a"],
         ["t", "p"]]

        And we are looking for words ["cat", "cap"].

        Let's see how backtracking works when it starts at row 0, column 0 (the letter "c"):

        1. Start at "c":
        - letter is "c".
        - Update trie node to the child node of "c".
        2. Explore Neighbors:
        - From "c", it looks at its neighbors. The right neighbor is "a".
        - Calls backtracking for "a".
        3. At "a":
        - Now, the function is exploring from "a".
        - It looks at its neighbors: "c" (visited) and "p".
        - Proceeds to "p" in separate recursive calls.
        4. Find Words:
        - When it reaches "p", it finds the complete words "cap".
        - Adds these words to matchedWords.
        5. Backtrack and Cleanup:
        After exploring one path (like "cap"), it backtracks, restoring the board and trie state to explore other paths (like "cap").
    '''

