"""Solution for LeetCode 3: Longest Substring Without Repeating Characters."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        highestcount = 0
        count = 0
        left = 0

        for char in s:
            if char not in word:
                word.add(char)
                count = len(word)
                highestcount = max(highestcount, count)
            else:
                while char in word:
                    word.remove(s[left])
                    left += 1

                word.add(char)
                count = len(word)
                highestcount = max(highestcount, count)

        return highestcount
