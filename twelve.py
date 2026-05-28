def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()

        # going through each character 
        for right in range(len(s)):
        	# if the right character is in the set already then remove left character from the window and slide away
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # add current character in the set
            char_set.add(s[right])

            # now updating the max length if current window is larger
            max_length = max(max_length, right - left + 1)

        return max_length

# space complexity is O(n) 
# time Complexity is O(n) or O(k) i.e. O(min(n, k))

#this is a sliding window probelm and hence I am using hash set. Going through each character and store it in the set while keeping count of the substring and pointing at first character of that sub string. The logic is to move forward until duplicate is found
