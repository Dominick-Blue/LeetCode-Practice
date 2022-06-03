class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num = 0; num < nums.length; num++) {
            int potentialMatch = target - nums[num];
            if (map.containsKey(potentialMatch)) {
                return new int[] {map.get(potentialMatch), num};
            }
            map.put(nums[num], num);
        }
        return null;
    }
}