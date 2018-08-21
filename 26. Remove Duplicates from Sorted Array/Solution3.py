"""
此处主要用到python的set功能，直接去重。OJ TOP 50%.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(list(set(nums)))
        return len(nums)
