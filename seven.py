#1) BFS (queue)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        # initializing queue
        queue = deque([""])

        for digit in digits:
            size = len(queue)
            for _ in range(size):
                # take each combination from the queue
                combo = queue.popleft()

                # appending each letter for each element in the queue to make the combination
                for letter in map[digit]:
                    queue.append(combo + letter)
    
        # list is need while returning
        return list(queue)

# time Complexity is O(4^n) - there are max 4 characters on each number
# space complexity is O(4^n) - storing all combinations at the same time so no backtracking

# First using BFS (queue), and not DFS(backtracking). Both data structures are possible, even the complexities are almost same. Only difference is in queue the stack overflow will never happen in any case and for DFS the space complexity is little more efficient as its not storing all the combination at the same time. Below are both solutions.

2) DFS(backtracking)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # storing all completed combinations
        result = []
        
        def backtrack(index, path):
            # already generated all combinations
            if index == len(digits):
                result.append("".join(path))
                return
            
            # getting all possible letters from the current digit
            letters = map[digits[index]]
            
            # geenrate possible combination for each digit
            for letter in letters:
                path.append(letter)          
                backtrack(index + 1, path)   
                path.pop()
        
        # starting backtracking from the first digit
        backtrack(0, [])
        
        return result


# time Complexity is O(4^n) - there are max 4 characters on each number
# space complexity is O(n)
