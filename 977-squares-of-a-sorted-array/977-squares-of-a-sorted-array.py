class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        new_list = [i ** 2 for i in nums]
        new_list.sort()
        return new_list