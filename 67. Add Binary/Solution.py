"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

"""
这种题对python，感觉有点cheating...OJ TOP30%.
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        dec_a = dec_b = 0

        for i in range(len_a):
            dec_a += int(a[i])<<(len_a-i-1)
        for j in range(len_b):
            dec_b += int(b[j])<<(len_b-j-1)
        return bin(dec_a +dec_b)[2:]
