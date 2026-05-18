class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> brackets = new HashMap<>();
        brackets.put('(', ')');
        brackets.put('{', '}');
        brackets.put('[', ']'); 
        char[] charArray = s.toCharArray();
        Stack<Character> charStack = new Stack<>();
        for (char c : charArray) {
            if (brackets.keySet().contains(c)) {
                charStack.push(c);
            } else if (brackets.values().contains(c)) {
                Character recent = charStack.peek();
                if (brackets.keySet().contains(recent)) {
                    if (!brackets.get(recent).equals(c)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
