class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        # starting with choosing first element
        for i in range(n - 3):
            # making sure we are choosing distinct second number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # choosing second number in the quadruplets
            for j in range(i + 1, n - 2):
                # making sure we are choosing distinct third number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # using two pointer method for remaining two numbers
                left, right = j + 1, n - 1

                while left < right:
                    # calculate the sum for all 4 numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # we found the target, now looking if we have more combinations
                        left += 1
                        right -= 1

                        # making sure we are choosing distinct third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # making sure we are choosing distinct fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # if sum is less than the target then move left
                    elif total < target:
                        left += 1
                    else:
                        # if sum is greater than target then move right
                        right -= 1

        return result


# time Complexity is O(3^n) - always need to check at least 3 numbers, given first would be the first number to no loop needed

# space complexity is O(n)

# the above logic is same as 3 sum, we choose first two unique numbers from quadruplets and then use two pointers method for remianing two numbers
