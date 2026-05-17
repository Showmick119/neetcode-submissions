class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        // Don't care about indexes here. Just want the number of
        // valid substrings. 'a' is a palindrome, since s.charAt(l)
        // equals s.charAt(r).

        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;

            // odd length
            while (l >= 0 && r < s.length() && l <= r &&
                s.charAt(l) == s.charAt(r)) {
                l--;
                r++;
                count++;
            }

            // even length
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && l <= r &&
                s.charAt(l) == s.charAt(r)) {
                l--;
                r++;
                count++;
            }

        }
        return count;
    }
}

/*
Here we are expanding out from the center. It is not like a standard
palindrome problem, where l is at start and r is at the end. 

String's total length being odd, doesn't mean it only contains odd
length palindromes. Same for even.

Like having the odd palindrome checker, helps us check for single
element palindromes like 'a'.

Even palindrome checker allows us to catch 'bb' from 'abba', whereas
an odd checker would have missed it. As it would have went straight to
catching 'aba'.

Hence, having both ODD and EVEN checker is beneficial and allows us to
hit everything.

Every position in your string could be:
1. The center of an odd-length palindrome
2. The left half of an even-length palindrome's center


## No Duplicates - Here's Why

Each palindrome has a **unique center**, so checking both odd and even centers at each position finds different palindromes:

## Example with "aaa"

At position i=0:
- **Odd center at 0**: Finds "a" (index 0)
- **Even center between 0-1**: Finds "aa" (indices 0-1)

At position i=1:
- **Odd center at 1**: Finds "a" (index 1) and "aaa" (indices 0-2)
- **Even center between 1-2**: Finds "aa" (indices 1-2)

At position i=2:
- **Odd center at 2**: Finds "a" (index 2)
- **Even center between 2-3**: Out of bounds, finds nothing

## The Key Insight

Each palindrome is discovered exactly once - when we're at its specific center:
- "aaa" is only found when center is at position 1 (odd)
- "aa" (0-1) is only found when center is between 0-1 (even)
- "aa" (1-2) is only found when center is between 1-2 (even)

**Different centers = different palindromes**, even if the characters 
are the same. The center position uniquely identifies each palindrome 
substring.

*/
