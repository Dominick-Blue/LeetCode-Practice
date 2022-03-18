from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        num_count = Counter(nums)
        
        for num in num_count:
            if num_count[num] >= 2:
                return True
            
            
        return False