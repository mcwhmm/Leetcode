#  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


'''2018.2.28 passed leetcode.com'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        size = len(s)
        i = 0

        if size < numRows or numRows == 1:
            return s

        for i in range(numRows):
            j = i
            result += s[j]
            while j < size:
                if i != 0 and i != numRows - 1:
                    j += 2 * (numRows - i) - 2  # 计算中间列
                    if j < size:
                        result += s[j]
                        j += 2 * i
                        if j < size:
                            result += s[j]
                else:
                    j += 2 * numRows - 2
                    if j < size:
                        result += s[j]
        return result