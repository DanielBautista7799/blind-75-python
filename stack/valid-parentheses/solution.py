from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"{":"}", "(":")", "[":"]"}
        stack = []
        for char in s:
            if char in dictionary:
                stack.append(char)
            else:
                if stack != []:
                    lastvalid = stack.pop()
                    if dictionary.get(lastvalid) == char:
                        continue
                    else:
                        return False
                else:
                    return False
        return stack == []
