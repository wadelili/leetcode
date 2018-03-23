#!python3


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = 2147483648
        ret = int(str(abs(x))[::-1])
        if x > 0 and ret <= MAX_INT:
            return ret
        elif x < 0 and ret <= MIN_INT:
            return -ret
        else:
            return 0