class Solution(object):
    def majorityElement(self, nums):
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            """
            paprestesnis sprendimas sios vietos:
            if n in count:
                count[n] += 1
            else: 
                count[n] = 1
            """
            
            if count[n] > maxCount:
                res = n
            maxCount = max(count[n], maxCount)
            
        return res
        