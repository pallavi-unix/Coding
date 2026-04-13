class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to store each string in the output list and then add all anagrams for it thats why we use defaultdict
        anagram_map = defaultdict(list)

        # lets go thorugh each word in a string
        for word in strs:
            count = 26 * [0]

            # counting each character from the word
            for char in word:
                count[ord(char) - ord('a')] += 1

            # coberting list to tuple so it can be used as a dictionary key
            key = tuple(count)

            # append each anagram to its corresponding key
            anagram_map[key].append(word)

        return list(anagram_map.values())



# time Complexity is O(nm) - n is number of strings, m is number of characters in the string

# space Complexity is O(nm) - n is number of strings, m is number of characters in the string

# Using dictionary so that we can have keys and value pair logic, need to return each string, just the difference between input and output is in output we are making group of the anagrams. Couting occurance of each character and stroing it to find the anagram. If we found the anagram with smae number of character occurances then append it to the dictionary
