class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # only has digits
        for token in tokens:
            if token[0] == '-' and len(token) > 1 and token[1:].isdigit():
                stack.append(int(token))
            elif token.isdigit(): ## won't work for number string which has a '-'
                stack.append(int(token))
            elif token == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 + op1)
            elif token == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif token == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
            elif token == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 / op1))
        return stack[-1]

"""
- given an array of strings called tokens that represent a valid arithmetic expression in
reverse polish notation
- operands may be integers or the results of other operations
- assume that division between integers always truncates toward zero
- can be a string representing an integer in range -200 to 200, INCLUSIVE
- for every operator, you pop() two elements
- the two elements can originally be there in the stack, or they can be a new one which was
created as a result of a previous operation
- int(a / b) will truncate towards zero and drop the fractional part, and also work for
negatives
- // just rounds left, towards smaller numbers. but this will take towards negative numbers,
we want to stay positive, hence we use int(), which just simply truncates.
- everytime there's an operator, you pop the last 2 elements of the stack, take the result
of the operation and then push it back into the stack.
- at the end, after you're done looping through tokens, your stack has one element left, and
you return that one element.
"""