def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    output = []
    n = len(nums)

    for i in range(n - 2):
        # avoding duplicate elements so that we can skip until next unique
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # when found unique elements we can choose next two elements
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                output.append([nums[i], nums[left], nums[right]])

                # making sure all three elements are unique and onlythen move the left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # again move so that we will not end up choosing same element
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return output

# time Complexity is O(n^2) - using 2 pointers
# space complexity is O(1) - have fixed numbers of variables

#The logic is very simple, to find three unique elements and add them if the sum is 0 then append them to the output. Using 2 pointers one from left and one from right, so initially I sorted the array so that first element can be fixed and other teo elements can be handle by 2 pointers
