"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

"""
对字符串进行轮询，复杂度为O（M*N）。对于随机均摊的字符串，复杂度为O（m+n）。
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_haystack = len(haystack)
        len_needle = len(needle)
        for i in range(len_haystack-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
