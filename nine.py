def maxArea(self, height: List[int]) -> int:
    left = 0
    output = 0
    right = len(height) - 1
    
    # exploring each node from left to right
    while left < right:
        # we need difference between left and right to calculate the max area covered
        diff = right - left
        # and we need min between left and right to multiply it with difference
        current = min(height[left], height[right])
        
        # calculating the difference
        area = diff * current

        # choosing max so find the container which stores the most water
        output = max(output, area)

        # only move left and right before they cross each other
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return output

# time Complexity is O(n) - have to explore each character from the string
# space complexity is O(1) - have fixed numbers of variables

# The logic is to use greedy algorithm because we need to explore each element just once, use it and calculate the output by multiplying 2 current elements. No need to go back. One variable going from left and another is coming from right. To form a container I should have min height and max width to calculate the max container storage. 
