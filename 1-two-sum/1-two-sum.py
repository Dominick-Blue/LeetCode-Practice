class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        results = {}
        
        for index,num in enumerate(nums):
            potential = target - num
            if potential in results:
                return [results[potential], index]
            else:
                results[num] = index
        