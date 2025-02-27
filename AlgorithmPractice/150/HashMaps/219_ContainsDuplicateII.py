# even though it's in the hashmap category, it made more 
# sense to use a sliding window set to track unique values
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set() # to track values in the sliding window
        l = 0 # left pointer (i)

        for r in range(len(nums)): # right pointer (j)
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False