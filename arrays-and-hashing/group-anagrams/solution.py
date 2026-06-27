"""Solution for Group Anagrams."""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for str in strs:
            countn = {}
            for char in str: 
                countn[char] = 1 + countn.get(char,0)
            key = tuple(sorted(countn.items()))
            if key in groups:
                groups[key].append(str)
            else:
                groups[key] = [str]
        return list(groups.values())