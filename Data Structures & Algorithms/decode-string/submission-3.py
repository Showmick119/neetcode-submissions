class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                curr_string = ""
                while stack[-1] != '[':
                    curr_string = stack.pop() + curr_string
                stack.pop()
                curr_num = ""
                while len(stack) > 0 and stack[-1].isdigit(): ## keep doing so while its still a number to *
                    curr_num = stack.pop() + curr_string
                curr_string *= int(curr_num)
                for i in curr_string:
                    stack.append(i)
                # stack.append(curr_string)
            else:
                stack.append(c)
        out = "".join(stack)
        return out