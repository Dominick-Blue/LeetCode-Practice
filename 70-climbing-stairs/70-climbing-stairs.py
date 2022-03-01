class Solution:
    def climbStairs(self, n: int) -> int:
        first_step, second_step = 1,1
        for i in range(n):
            first_step, second_step = second_step, first_step + second_step
        return first_step
        