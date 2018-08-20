"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
单循环实现哈希表及查找。总复杂度为O(n)，LeetCode OJ Runtime: 40ms. TOP15%.
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for i in range(len(nums)):
            if a.get(nums[i]) is None:
                a[nums[i]] = i
            sol = target-nums[i]
            if sol in a.keys():
                if a[sol] != i:
                    return a[sol], i
