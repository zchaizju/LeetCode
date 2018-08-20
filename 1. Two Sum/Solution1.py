"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
此解法为对原始list的暴力搜索，取双循环，复杂度为O(nlogn)，LeetCode OJ Runtime: 1320 ms.
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            a = nums[i]
            sol = target-a
            if sol in nums[i+1:]:
                j = nums[i+1:].index(sol)+i+1
                return i, j
