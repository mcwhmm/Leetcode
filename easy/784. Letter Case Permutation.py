# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
#
# Note:
#
#     S will be a string with length at most 12.
#     S will consist only of letters or digits.


'''2018.2.26. passed leetcode.com'''


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        result.append(S)
        length = len(S)
        '''从左向右依次大写字母，每改写一位即追加到结果表。直到遍历所有字母的。'''
        for i in range(length):                                 #遍历字符串中的每一位
            lenResult = len(result)
            for num in range(lenResult):                        #遍历目前结果表
                strList = list(result[num])                     #从结果取出一行字符串
                if strList[i].isalpha():                        #如果第i位是字母
                    if strList[i].islower():                    #如果字母是小写
                        strList[i] = strList[i].upper()         #变大写
                    else:
                        strList[i] = strList[i].lower()         #否则变小写
                    result.append(''.join(strList))             #将此修改后的字符串加到结果

        return result
