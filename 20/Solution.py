class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for e in s:
            if e == '{' or e == '(' or e == '[':
                strs.append(e)
            else:
                if len(strs) == 0:
                    return False
                f = strs.pop(-1)
                if e == '}' and f != '{':
                    return False
                elif e == ')' and f != '(':
                    return False
                elif e == ']' and f != '[':
                    return False

        return len(strs) == 0

solution = Solution();
print(solution.isValid("([)]"));
