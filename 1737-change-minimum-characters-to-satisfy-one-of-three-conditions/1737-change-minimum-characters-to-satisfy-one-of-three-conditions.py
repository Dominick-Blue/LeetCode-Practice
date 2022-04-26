from collections import Counter

class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
        letters = 'abcdefghijklmnopqrstuvwxy'
        
        len_a = len(a)
        len_b = len(b)
        
        count_a = Counter(a)
        count_b = Counter(b)
        
        def get_min_ops(first_count, second_count):
            min_ops = float('inf')
            ops_a = sum(first_count.values())
            ops_b = 0
            
            for char in letters:
                ops_a -= first_count[char]
                ops_b += second_count[char]
                min_ops = min(min_ops, ops_a + ops_b)
            
            return min_ops
        
        condition1 = get_min_ops(count_a, count_b)
        condition2 = get_min_ops(count_b, count_a)
        condition3 = len_a - max(count_a.values()) + len_b - max(count_b.values())
        
        return min(condition1,condition2,condition3)