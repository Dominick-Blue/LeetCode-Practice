class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)
        n = len(nums) + 1
        
        for num in range(n):
            if num not in num_set:
                return num