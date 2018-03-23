#!python3

# 这道题的转换规则很不明确，提交了两次都没通过，已然放弃

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        num, has_num, has_decimal = "", False, False
        for c in str:
            if has_num is False and (c == "+" or c == "-"):
                num = c + "0"
                continue

            if "0" <= c <= "9":
                has_num = True
                num += c
            elif has_num:
                if has_decimal is False and c == ".":
                    has_decimal = True
                    num += "."
                else:
                    break

        num = int(num) if num != "" else 0
        if num < MIN_INT:
            num = MIN_INT
        elif num > MAX_INT:
            num = MAX_INT

        return num