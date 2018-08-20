"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
此解法为对哈希表搜索，取双循环，循环1用于生成dict，循环2用于查找。总复杂度为O(n)，LeetCode OJ Runtime: 48ms.
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
            if nums[i] in a.keys():
                a[nums[i]].append(i)
            else:
                a[nums[i]] = [i]
    
        for i in range(len(nums)):
            sol = target-nums[i]
            if sol in a.keys():
                for j in a[sol]:
                    if j != i:
                        return i, j
