#!python3


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s

        z_list = [''] * numRows
        index, step = 0, 1
        for x in s:
            z_list[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(z_list)