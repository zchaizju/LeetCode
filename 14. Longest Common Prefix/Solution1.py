"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

"""
解法1： 暴力搜索；对第一个str的所有前缀进行遍历，对每个前缀，遍历所有其他str。直到匹配。OJ Runtime：TOP 80%。算法复杂度：O(mn).m为str长度，n为str个数。
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        common_prefix = ''
        for i in range(len(strs[0])):
            common_num = 0
            for j in range(1, len(strs)):
                if strs[j].startswith(strs[0][:i+1]):
                    common_num += 1
            if common_num == len(strs)-1:
                common_prefix = strs[0][:i+1]
        return common_prefix
