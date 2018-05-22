class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = maxI = maxJ = water = 0
        j = len(height) - 1
        while i < j:
            if height[i] > maxI:
                maxI = height[i]
            else:
                water += maxI - height[i]

            if height[j] > maxJ:
                maxJ = height[j]
            else:
                water += maxJ - height[j]

            if maxI < maxJ:
                i += 1
            else:
                j -= 1

        return water

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size < 1:
            return 0
        beg = end = temp = water = idx = 0
        maxHeight = max(height)
        for n in range(size):
            if height[n] >= beg:
                beg = height[n]
                water += temp
                temp = 0
            else:
                temp += beg - height[n]
            if height[n] == maxHeight:
                idx = n
                temp = 0
                break

        for m in range(size - 1, idx - 1, -1):
            if height[m] >= end:
                end = height[m]
                water += temp
                temp = 0
            else:
                temp += end - height[m]

        return water

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([2,0,2]))