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
        '''�����������δ�д��ĸ��ÿ��дһλ��׷�ӵ������ֱ������������ĸ�ġ�'''
        for i in range(length):                                 #�����ַ����е�ÿһλ
            lenResult = len(result)
            for num in range(lenResult):                        #����Ŀǰ�����
                strList = list(result[num])                     #�ӽ��ȡ��һ���ַ���
                if strList[i].isalpha():                        #�����iλ����ĸ
                    if strList[i].islower():                    #�����ĸ��Сд
                        strList[i] = strList[i].upper()         #���д
                    else:
                        strList[i] = strList[i].lower()         #�����Сд
                    result.append(''.join(strList))             #�����޸ĺ���ַ����ӵ����

        return result
