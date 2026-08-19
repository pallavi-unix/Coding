class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)

# time Complexity is O(1)
# space complexity is O(1)

# using XOR which gives the sum of two bits without carrying anything, AND finds where a carry is needed, I keep doing this until there is no carry left, and then we have the final sum.
