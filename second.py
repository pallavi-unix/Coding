class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
	    first = [1] * n
	    last = [1] * n
	    output = [1] * n

	    # first lets calculate for first element
	    for i in range(1, n):
	        first[i] = first[i - 1] * nums[i - 1]

	    # calculating product for the elements that are in the middle
	    for i in range(n - 2, -1, -1):
	        last[i] = last[i + 1] * nums[i + 1]

	    # calculating product for the last element
	    for i in range(n):
	        output[i] = first[i] * last[i]

	    return output


# time Complexity is O(n) - n is number of elements and have to explore each element
# space Complexity is O(n)

# The logic is to calculate first and last elements product separately to avoid extra loops.
