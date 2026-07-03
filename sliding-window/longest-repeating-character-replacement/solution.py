"""Solution for LeetCode 424: Longest Repeating Character Replacement."""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        currentbest = 0
        maxfreq = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxfreq = max(maxfreq, count[s[right]])

            repl = (right - left + 1) - maxfreq

            while repl > k:
                count[s[left]] -= 1
                left += 1
                repl = (right - left + 1) - maxfreq

            currentbest = max(currentbest, right - left + 1)

        return currentbest
