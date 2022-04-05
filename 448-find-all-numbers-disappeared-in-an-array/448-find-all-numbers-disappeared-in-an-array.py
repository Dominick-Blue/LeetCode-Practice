class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        num_set = set(nums)
        n = len(nums) + 1
        missing_nums = []
        
        for num in range(1, n):
            if num not in num_set:
                missing_nums.append(num)
        return missing_nums