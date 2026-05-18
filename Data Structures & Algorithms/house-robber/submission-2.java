class Solution {
    public int rob(int[] nums) {
        // CANNOT ROB TWO ADJACENT HOUSES (back to back indices)
        // SO IT'S ESSENTIALLY A COMBINATION OF (i) & (i + 1) INDICES
        int pass1 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (2 * i < nums.length) {
                pass1 += nums[2 * i];
            }
        }
        int pass2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (2 * i + 1 < nums.length) {
                pass2 += nums[2 * i + 1];
            }
        }
        return (pass1 > pass2) ? pass1 : pass2;
    }
}
