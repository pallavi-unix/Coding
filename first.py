def topKFrequent(nums, k):
	# default dict is used to get all elemnets into dic as a key, and their ferquency will be there values
    result = []
    freq = defaultdict(int)
    
    # getting frequency for each character 
    for num in nums:
        freq[num] += 1

    # now to find first first K elements who are frequent hence need a bucket sorting
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # just get first k elements from the bucket
    
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result



# time Complexity is O(n) - n is number of elements, have to explore each element
# space Complexity is O(n)

# The logic is to get a frequency of each element into the dict and then use bucket sorting logic to get first k elements