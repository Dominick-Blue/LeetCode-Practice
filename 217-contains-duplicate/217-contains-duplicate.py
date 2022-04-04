class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hist = {}
        
        for num in nums:
            if num in hist:
                return True
            else:
                hist[num] = 1
        return False