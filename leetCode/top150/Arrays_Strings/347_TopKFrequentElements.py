class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        # creates a bucket (list of lists), length is one more than the size of nums
        # index represents a frequency count
        freq = [[] for i in range(len(nums) + 1)]
        # alt way: freq = defaultdict(list)

        for n in nums:
            # count each time a value occurs
            count[n] = 1 + count.get(n, 0)

        # places each numbver into the bucket that corresponds to its frequency (c)
        # if a number appears c times, it is appended to the list at freq[c]
        for n, c in count.items():
            freq[c].append(n)

        res = []


        # The loop starts at index ′len(freq) - 1′.
        # It stops before reaching ′0′ (so it iterates until index 1).
        # Each iteration, the loop decrements ′i′ by 1.
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res