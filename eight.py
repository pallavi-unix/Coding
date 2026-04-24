def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        # get a starting closest sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                # get a closest sum for current triplets
                current_sum = nums[i] + nums[left] + nums[right]
                
                # if the current sum is closer than previous one then update it
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # if current sum is less than target then move forard with left
                if current_sum < target:
                    left += 1
                # if current sum is greater than taget then decrease right
                elif current_sum > target:
                    right -= 1
                # if above two conditions are not matching that means we found the current sum as target
                else:
                    return current_sum 
        
        return closest_sum


# time Complexity is O(n^2) - using 2 pointers
# space complexity is O(1) - have fixed numbers of variables

# Same like sum 3, this problem uses 2 pointer method. Only difference in this problem is we need to find addition for three elements to closest or same as the given target and return the sum.

