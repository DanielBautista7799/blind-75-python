"""Solution for LeetCode 125: Valid Palindrome."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()

        return clean == clean[::-1]
