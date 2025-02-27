from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = defaultdict(int) # num : index

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        