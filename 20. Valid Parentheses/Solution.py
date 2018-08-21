"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

"""
好聚好散，此题堆栈。
OJ TOP80%.
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')':'(', ']':'[','}':'{'}
        stack = []
        for ch in s:
            if ch in dict.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if dict[ch] != left:
                    return False
        if stack != []:
            return False
        return True
