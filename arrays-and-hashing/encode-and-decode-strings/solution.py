"""Solution for LeetCode 271: Encode and Decode Strings."""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            count = len(word)
            s += str(count) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        array = []

        while len(s) > 0:
            i = 0
            count = ""

            while s[i] != "#":
                count += s[i]
                i += 1

            countint = int(count)
            s = s[i + 1:]
            word = s[:countint]
            array.append(word)
            s = s[countint:]

        return array
