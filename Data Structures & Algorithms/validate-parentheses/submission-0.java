class Solution {
    public boolean isValid(String s) {
        char[] cArray = s.toCharArray();
        if (cArray[0] == '(') {
            if (cArray[s.length() - 1] == ')') {
                return true;
            }
        } else if (cArray[0] == '{') {
            if (cArray[s.length() - 1] == '}') {
                return true;
            }
        } else if (cArray[0] == '[') {
            if (cArray[s.length() - 1] == ']') {
                return true;
            }
        }
        return false;
    }
}
