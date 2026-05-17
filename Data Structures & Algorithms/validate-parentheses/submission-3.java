class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] arr = s.toCharArray();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        for (char c : arr) {
            if (!stack.empty() && map.keySet().contains(c)) {
                if (stack.peek().equals(map.get(c))) {
                    stack.pop();
                } else {
                    return false;
                    // in this step we are specifically adding closing
                    // so the opening must match. We are adding a pair.
                    // so match is mandatory, otherwise false.
                }
            } else {
                stack.push(c);
            }
        }
        return stack.empty();
    }
}
