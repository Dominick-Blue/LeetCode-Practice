class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        var dieterPoints = 0;
        int windowStart = 0, totalCalories = 0;
        
        for (int windowEnd = 0; windowEnd < calories.length; windowEnd++) {
            totalCalories += calories[windowEnd];
            
            if (windowEnd >= k - 1) {
                if (totalCalories < lower) {
                    dieterPoints--;
                } else if (totalCalories > upper) {
                    dieterPoints++;
                }
                totalCalories -= calories[windowStart++];
            }
        }
        return dieterPoints;
    }
}
