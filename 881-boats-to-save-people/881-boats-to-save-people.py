class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()
        left, right = 0, len(people) - 1
        min_boats = 0
        
        while left <= right:
            min_boats += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        
        return min_boats
        