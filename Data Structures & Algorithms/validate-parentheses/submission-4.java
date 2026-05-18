class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();
        // what's being added is a bigger force than what's there alr
        map.put(')', '(');
        map.put('}', '{' );
        map.put(']', '[');
        char[] arr = s.toCharArray();
        for (char c : arr) {
            if (map.keySet().contains(c)) {
                if (map.values().contains(stack.peek())) {
                    if (stack.peek().equals(map.get(c))) {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            } else {
                stack.push(c);
            }
        }
        return stack.empty();
    }
}
