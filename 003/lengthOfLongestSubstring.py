#!python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        len = 0
        sub_str = ""
        for c in s:
            i = sub_str.find(c)
            if i == -1:
                sub_str += c
                len += 1
            else:
                sub_str = sub_str[i + 1:] + c
                len = len - i
            if len > max_len:
                max_len = len

        return max_len