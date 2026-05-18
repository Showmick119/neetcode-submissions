class Solution {
    public int numDecodings(String s) {
        // considering a simple edge case:
        if (s.length() == 1) {
            return 0;
        }

        int[] dp = new int[s.length() + 1];
        // for final element, there is always 1 way to map it. Even if
        // it's 0
        dp[s.length()] = 1;

        // if string starts with 0, we immediately stop, as we cannot
        // create a valid mapping from that
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '0') {
                dp[i] = 0;
            } else {
                dp[i] = dp[i + 1];
                if (i + 1 < s.length() && (s.charAt(i) == '1' ||
                    s.charAt(i) == '2' && s.charAt(i + 1) < '7'))
                    dp[i] += dp[i + 2];
            }
        }

        return dp[0];
    }
}

/*
- We don't actually have to map it to characters. We just need to know
and validate, that it does map to SOMETHING.
- So the real challenge is picking the combinations, and the fact that
0 cannot be a leading zero to any of the number combinations.
- Can have numbers from 1 through 26. Not less and not more.
- We are using a decision tree type structure.
- For values above 26, it's better to just use two seperate characters.
- Only use 2 characters for values between 10 and 19.
- If first digit of the group, starts with 2, then next digit must be
between 0 and 6.
- If first digit of the group starts with 1, then next digit must be
between 0 and 9.
- First digit of group or single group can never start with a 0.
- We will only have 2 branches if our first letter is a 1 or 2.
- Using decision tree would be an exponential Big-O, hence take a
bottom up approach.
*/