class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        cycle = 2 * numRows - 2 # this formula helps calculate zigzag pattern

        # calculate the string row by row
        for row in range(numRows):
            for i in range(row, len(s), cycle):
                # adding vertical character 
                result.append(s[i])

                # adding diagonal position
                diagonal = i + cycle - 2 * row
                # checking if we are not at the end of the string
                if row != 0 and row != numRows - 1 and diagonal < len(s):
                    result.append(s[diagonal])

        return "".join(result)


# space complexity is O(n) 
# time Complexity is O(n)

# Dynamic List is the data structure I used because its mutable and hence efficient. Going zigzag means going vertically down and diagonally go. Now by calculating one character per cycle we get their position means row by row and then place them into string.
