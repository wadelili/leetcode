#!python3

# 1、给定一个无序的数组，求出一个数，使得其左边的数都小于它，右边的数都大于等于它
# 2、给定一个无序的数组，求出使得其左边的数都小于它，右边的数都大于等于它的所有数字


class Solution:
    def findMiddleNum(self, nums):
        """
        :type nums: list
        :rtype: int
        """
        target = 0
        l_max = nums[0]
        is_ext = True
        for i in range(1, len(nums)):
            if is_ext and nums[target] > nums[i]:
                is_ext = False
            elif is_ext is False and nums[i] > l_max:
                is_ext = True
                target = i

            if nums[i] > l_max:
                l_max = nums[i]

        return target if is_ext else -1

    def findMiddleNums(self, nums):
        """
        :type nums: list
        :rtype: list
        """
        size = len(nums)
        l_max_list = []
        l_max = 0
        for i in range(0, size):
            l_max_list.append(l_max)
            if nums[i] > l_max:
                l_max = nums[i]

        res = []
        r_min = nums[size - 1]
        for i in range(0, size)[::-1]:
            if l_max_list[i] < nums[i] <= r_min:
                res.insert(0, i)
            if nums[i] < r_min:
                r_min = nums[i]

        return res