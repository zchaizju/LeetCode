"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

"""
复杂度O(2*n), OJ top20%.
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num = ''
        for i in digits:
            str_num += str(i)
        new_num = int(str_num)+1
        digits_plus_one = []
        for j in str(new_num):
            digits_plus_one.append(int(j))
        return digits_plus_one
