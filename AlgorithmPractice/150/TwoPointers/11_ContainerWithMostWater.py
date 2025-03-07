class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

    # runtime O(n), where n is the length of the height array
    # memory O(1), because we only use pointers, which require
    # constant space no matter the input size