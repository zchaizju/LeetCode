"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

"""
此题即简单的求x的根号，返回int整型。可用牛顿迭代法求解，TOP10%.
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1.0
        while (True):
            j = (i+x/i)/2.0
            if (abs(i-j) < 0.000000000005):
                break
            i = j
        return int(j)
