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
解法2仍为暴力搜索，但可读性十分高，十分有学习的必要。复杂度同Solution1。OJ Runtime：40ms；TOP15%.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest_str = min(strs, key=len)
        for i, ch in enumerate(shortest_str):
            for other in strs:
                if other[i] != ch:
                    return shortest_str[:i]
        return shortest_str
