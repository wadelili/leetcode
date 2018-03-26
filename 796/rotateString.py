#!python3

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) or set(A) != set(B):
            return False

        if A == "":
            return True

        i = 0
        for c in A:
            if B[0] == c and B == A[i:] + A[:i]:
                return True
            i += 1

        return False
