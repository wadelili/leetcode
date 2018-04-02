#!python3


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        size = len(s)
        last = size // 2
        for i in range(0, last + 1):
            if i == last and (i == size - i - 1 or s[i] == s[size - i - 1]):
                return True
            if s[i] != s[size - i - 1]:
                break

        return False

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]