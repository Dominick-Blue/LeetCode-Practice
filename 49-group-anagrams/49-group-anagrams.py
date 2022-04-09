class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Create a dictionary using defaultdict
        # Assign sorted strings to dictionary on pass 1
        # Compare strings in str on pass 2 and if they match a key in the dictionary, append result
        # Return result
        
        key_map = defaultdict(list)
        
        for s in strs:
            arr = [0] * 26
            for l in s:
                arr[ord(l) - ord('a')] += 1
            key_map[tuple(arr)].append(s)
        
        return key_map.values()
            