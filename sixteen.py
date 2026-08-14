class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # we are using slide the window across the array logic
        for i in range(k, len(nums)):
            # removing the element that is leaving the window
            window_sum += nums[i] - nums[i - k]
            # adding new element that is entering the window
            max_sum = max(max_sum, window_sum)

        # getting maximum average
        return max_sum / k

# time Complexity is O(n)