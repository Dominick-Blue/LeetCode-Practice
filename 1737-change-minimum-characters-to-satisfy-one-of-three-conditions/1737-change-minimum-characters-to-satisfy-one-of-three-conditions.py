from collections import Counter

class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        n_a = len(a)
        n_b = len(b)
        
        count_a = Counter(a)
        count_b = Counter(b)
        
        def change(c_a, c_b):
            ans = sys.maxsize
            op_a = sum(c_a.values())
            op_b = 0
            
            for c in "abcdefghijklmnopqrstuvwxy":
                op_a -= c_a[c]
                op_b += c_b[c]
                ans = min(ans, op_a + op_b)
                
            return ans
        
        ans1 = change(count_a, count_b)
        ans2 = change(count_b, count_a)
        ans3 = n_a - max(count_a.values()) + n_b - max(count_b.values())
        
        return min(ans1, ans2, ans3)
        
        