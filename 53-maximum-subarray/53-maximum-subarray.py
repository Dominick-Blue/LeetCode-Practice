class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sub = max_sub = nums[0]
        
        for num in nums[1:]:
            current_sub = max(num, current_sub + num)
            max_sub = max(max_sub, current_sub)
        
        return max_sub