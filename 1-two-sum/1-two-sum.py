class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], index]
            dict[num] = index
                
            