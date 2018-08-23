"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

"""
此题解法复杂度为O(n)。以下是LeetCode上名为Google的用户提出的巨nice的code。后来得知这个算法名为Kadane's algorithm。见链接https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for i in nums[1:]:
            curSum = max(i, curSum+i)
            maxSum = max(maxSum, curSum)
        return maxSum
