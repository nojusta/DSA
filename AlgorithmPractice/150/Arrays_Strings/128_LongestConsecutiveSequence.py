class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        numSet = set(nums)
        longest = 0

        # iterate through set instead of array to improve efficiency if there are duplicate values
        for n in numSet:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
# Runtime: O(n), where n is the number of elements in the input list
# numSet takes O(n) time, first loop is O(n) and inner loop runs O(n) at most,
# which boils down to O(n), since we ignore constant values in big O notation

# Memory: O(n), because the set stores all uniqe elemenets from the input list
