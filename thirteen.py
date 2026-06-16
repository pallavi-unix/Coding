class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backTrack(current, openCount, closeCount):
        	# if we already reached to 2 * n characters then result is done and return it
            if len(current) == 2 * n:
                result.append(current)
                return

            # if open count is less than "n" then add more
            if openCount < n:
                backTrack( current + "(", openCount + 1, closeCount)

            # if close count is less than open count then add more
            if closeCount < openCount:
                backTrack( current + ")", openCount, closeCount + 1)

        # this is for starting the backtracing operation with empty string and zero
        backTrack("", 0, 0)
        return result


# this is catalan number growth time and space complexity, as the every single time the "n" incraeses the number of operations also grows with it, so does number of valid parantheses. Each string has length 2n

# number of valid combinations * length of each combination

# When you try all possible combination the in algorithms like this every time n increases by 1 the operation becomes 4 times hence 4 raise to n

# not all coices are valid, becasue we have 1 close paranthese for every open parantheses hence we are removing invalid once thats why divided by square root of n

# time complexity is O(4^n / square root(n)) 

# space complexity is O(4^n / square root(n))

# DFS is best approach for below problem. We need to use backtracing by generating all possible sequences while cutting down invalid ones from the begining. The logic is to use valid parantheses to generate all possible combination and check weather they are unique or not. Catalan number growth concept is best way to implement that logic. The given constraint is 1 <= n <= 8. With all possible combination we will get 2 * n number of characters in the result string.
