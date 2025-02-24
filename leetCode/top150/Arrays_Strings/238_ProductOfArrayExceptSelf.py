class Solution(object):
    def productExceptSelf(self, nums):
        # Initialize res with ones; using ones for multiplication.
        res = [1] * len(nums)

        # First loop: accumulate the product of all elements to the left (prefix products)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix         # set left product for current index
            prefix *= nums[i]       # update prefix product

        # Second loop (runs in reverse): accumulate the product of all elements to the right (postfix products)
        postfix = 1
        # The range function here is set up as:
        # range(start, stop, step)
        # start = len(nums) - 1  -> the last index
        # stop = -1              -> stop before -1, so the loop includes index 0
        # step = -1              -> move from the end of the list to index 0, decrementing by 1 each time
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix       # multiply by postfix to combine left and right products
            postfix *= nums[i]      # update postfix product

        return res