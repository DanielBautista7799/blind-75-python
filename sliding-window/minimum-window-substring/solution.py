"""Solution for LeetCode 76: Minimum Window Substring."""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        countT = {}
        window = {}
        best = ""
        bestlen = float("inf")

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        need = len(countT)
        have = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if right - left + 1 < bestlen:
                    best = s[left : right + 1]
                    bestlen = right - left + 1

                leftchar = s[left]
                window[leftchar] -= 1

                if leftchar in countT and window[leftchar] < countT[leftchar]:
                    have -= 1

                left += 1

        return best
