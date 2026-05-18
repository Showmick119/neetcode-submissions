class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put('[', ']');
        map.put('(', ')');
        map.put('{', '}');
        char[] sChar = s.toCharArray();
        for (char c : sChar) {
            if (!stack.isEmpty() && map.keySet().contains(stack.peek())) {
                if (c != map.get(stack.peek())) {
                    return false;
                } else {
                    stack.push(c);
                }
            }
        }
        return true;
    }
}
