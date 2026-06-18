class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.isdigit():
                stack.append(int(op))
            elif op == "D":
                top = stack[-1]
                stack.append(top * 2)
            elif op == "+":
                first = stack.pop()
                second = stack.pop()
                total = first + second
                stack.append(first)
                stack.append(second)
                stack.append(total)
            elif op == "C":
                stack.pop()
        return sum(stack)

"""
- you are keeping scores for a baseball game with strange rules. at the beginning of the
game, you start with an empty record.
- given a list of strings, where ops[i] is the ith op you must apply to the record, and is
one of the following:
- record a new score of x, + is record a new score that is the sum of the two previous
scores, D is record a new score that is the double of the previous score, C is invalidating
the prev score and removing it from the record.
- return sum of all scores on the record after applying all ops.
"""