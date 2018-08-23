"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

"""
此题没什么技巧，主要是下一个数字取决于上一数字的code。因此需要对n之前的所有数字进行遍历，然后对n-1的code，逐位进行count。
这个题目刚开始考虑用字典实现，还是很方便的。但是写完之后发现一个致命问题，就是字典的键值必须是unique的，然而在实际统计中，可能出现
"112211"这种情况，那么1就会count为4，如果要count成两个2还是略有麻烦，因此最终放弃了字典。
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        coded_i = '1'
        i = 2
        while i <= n:
            last_code = coded_i
            coded_i = ''
            j = 0
            while j < len(last_code):
                num = last_code[j]
                count = 1
                j += 1
                while j < len(last_code) and last_code[j] == num:
                    count += 1
                    j += 1
                coded_i += (str(count)+num)
            i += 1
        return coded_i
