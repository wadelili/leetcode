#!python3


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0


if __name__ == "__main__":
    num = 13
    assert (Solution().canWinNim(num) is True)
    num = 4
    assert (Solution().canWinNim(num) is False)