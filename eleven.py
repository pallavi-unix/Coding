class Solution:
    def reverse(self, x: int) -> int:
        # as we are not allowed to store 64 bit integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # consider all numbers equally instead of negative/positive
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        # converting number digit by digit
        while x > 0:
            digit = x % 10
            x //= 10

            # check before updating the result
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        result *= sign

        # to check if we are not going over the 32 bit range
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result

# time Complexity is O(n)
# space complexity is O(1)

#The logic is to reverse the number digit by digit and store in 32 bit range, if overflows then return 0. The formula is to work on positive integers so if the input is negative then convert it to positive first then follow the same formula
