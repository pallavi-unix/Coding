def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
    	# check if num - 1 is not the case hence the num is a first element in the consecutive sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            # keep going until next consecutive number
            while current + 1 in num_set:
                current += 1
                length += 1

            # updating the longest consecutive sequence
            longest = max(longest, length)

    return longest


# time Complexity is O(n)
# space Complexity is O(n)