class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        complement_map = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [index, complement_map[complement]]
            complement_map[num] = index
        
        
                