class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_amt_of_water = 0
        
        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            max_amt_of_water = max(max_amt_of_water, area)
            
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
            
        
        return max_amt_of_water
        
        