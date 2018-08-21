"""

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

"""
考虑到题目中的follow up，考虑不采用str函数实现回文数字。主要思路：把数字对半拆开，对比左右两部分。每次对x除10进行循环，因此算法复杂度为O(log10(n))。
OJ Runtime为744ms，时间较长。
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        rev_x = 0
        while rev_x < x:
            rev_x = x%10 + rev_x*10
            x = int(x/10)
        return (x == rev_x or x == int(rev_x/10))
