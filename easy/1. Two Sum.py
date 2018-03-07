# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

'''2018.2.28'''
'''passed'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in nums:

            if target - i in nums and target - i != i:
                if target - i > i:
                    result = [nums.index(i), nums.index(target - i)]
                    return result
                result = [nums.index(target - i), nums.index(i)]
                return result

            if target - i in nums and target - i == i:
                for n in range(len(nums)):
                    if nums[n] == target -i:
                        result.append(n)
                        if len(result) == 2:
                            return result

							
#print(Solution().twoSum([3,3], 6))
