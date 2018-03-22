#!python3


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_str = ""
        size = len(s)
        longest = 0
        for i in range(size):
            j, long = 1, 1
            while i - j > -1 and i + j < size:
                if s[i - j] != s[i + j]:
                    break
                long += 2
                j += 1

            if long > longest:
                longest = long
                longest_str = s[i - j + 1:i + j]

            if i - 1 > -1 and s[i - 1] == s[i]:
                j, long = 1, 2
                while i - 1 - j > -1 and i + j < size:
                    if s[i - 1 - j] != s[i + j]:
                        break
                    long += 2
                    j += 1

                if long > longest:
                    longest = long
                    longest_str = s[i - j:i + j]

                continue

        return longest_str

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        start = 0
        max_length = 1
        for i in range(len(s)):
            if i - max_length >= 1 and s[i - max_length - 1:i + 1] == s[i - max_length - 1:i + 1][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 1] == s[i - max_length:i + 1][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length]