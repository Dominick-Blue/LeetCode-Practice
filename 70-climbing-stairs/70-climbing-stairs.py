class Solution:
    def climbStairs(self, n: int) -> int:
        #We initialize our dp array.
        #dp Index: this will be the step number we are currently on
        #dp Value: This will be the number of unique ways we are able to get to this current step.
        
        
        #We initialize our dp array with dp[0] = 1 and dp[1] = 1. Only one way of getting to the top when there are zero
        #Stairs, do nothing. Only one way to get to the top when there is only one step, take one step
        
        #Now we iterate through the rest of our array. We say that the number of ways to get to the current step
        #is the number of ways from the previous step plus the number of ways from two steps ago. This is because
        #Our only moves from those steps are to move one or two steps
            
        #We return the last step
        
    
        dp = [0] * (n+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i - 2]
            
        return dp[n]