# -*- coding: utf-8 -*-：

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#

'''
在PyCharm python 3.6 编译通过
但无法通过leetcode.com编译，错误如下：
Runtime Error Message: Line 29: ValueError: invalid literal for int() with base 10: ''
Last executed input: 0
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = []
        flag = 0
        x = list(str(x))
        if not x[0].isdigit():
            result.append(x[0])
            for i in range(len(x)-1, 0, -1):
                if x[i] == 0 and flag == 0:
                    continue
                if x[i] != 0:
                    flag = 1
                if flag == 1:
                    result.append(x[i])
        else:
            for i in range(len(x)-1, -1, -1):
                if x[i] == "0" and flag == 0:
                    continue
                if x[i] != 0:
                    flag = 1
                if flag == 1:
                    result.append(x[i])

        return int(str(''.join(result)))

print(Solution().reverse(-123))
print(Solution().reverse(1230))
print(Solution().reverse(-1230))

