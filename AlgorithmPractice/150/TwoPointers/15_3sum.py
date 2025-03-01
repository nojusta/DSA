class Solution(object):
    def threeSum(self, nums):
        res = []  # return the result as a list of lists (bucket)
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            # avoid reusing the same value
            if i > 0 and a == nums[i - 1]:
                continue  # skip current iteration of loop

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res