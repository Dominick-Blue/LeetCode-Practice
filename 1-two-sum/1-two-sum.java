class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            int firstNum = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                int secondNum = nums[j];
                if (firstNum + secondNum == target) {
                    return new int[] {i,j};
                }
            }
        }
        return null;
    }
}