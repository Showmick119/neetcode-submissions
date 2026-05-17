class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // assume 1-indexed array, so always shift actual index by +1
        // index 2 > index 1 and they don't have to be consecutive
        // two pointers!
        int L = 0;
        int R = numbers.length - 1;
        while (L < R) {
            if ((numbers[L] + numbers[R]) > target) {
                R--;
            } else if ((numbers[L] + numbers[R]) < target) {
                L++;
            } else {
                return new int[]{(L + 1), (R + 1)};
            }
        }
        return new int[]{};
    }
}
