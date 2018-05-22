class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        area = 0
        while i < j:
            thisArea = (j - i) * min(height[i], height[j])
            if thisArea > area:
                area = thisArea
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area