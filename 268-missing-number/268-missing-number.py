class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0
        
        for num in range(1, len(nums)):
            expected_num = nums[num - 1] + 1
            if nums[num] != expected_num:
                return expected_num