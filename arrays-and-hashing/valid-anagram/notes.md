# Valid Anagram — Notes

## First Thoughts

Inital thoughts are to write out each charater for each and mark them off as we see them leaving them with nothing at the end if valid and the letters that do not match if invalid.

## Independent Attempt

- **Attempt time:** 20 minutes

## Brute-Force Approachclass Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for char in s:
                if char in t:
                    t = t.replace(char, "" ,1)
            if t == "":
                return True

            else:
                return False
        return False


This approach used my initial thoughts as the basis for creating worked by going for every character in s and deleting it if seen in t only once by the end if there was nothing left in t then they were the same. However too slow.

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(t) == sorted(s)

This approach was used after I found out str could be sorted in python however still too slow for the problem.


## Optimized Approach

The optimized approach is not very complex in terms of code but its just the reitteratino and being able to make sure what each call is doing is what the difficulty of this problem is. Initally make sure they are the same length. Then for the length of one (either doesnt matter which as they must be same length) we get the current letter we are at and set it as a key for counts and countt then we go to the next letter if it is repeated we increase count default count being 0 and adding 1 to the value of the letter each time we see it. Lastly we compare the countt and counts to see if they are the same if not then they are not anagrams.

- **Data structure / pattern:** 
HashMap
- **Time complexity:**
O(n+m)
- **Space complexity:**
0(1)
## Mistakes and Debugging

- Struggled to figure out how to cut down time. Used different approaches but ultimately realized that count was the most important thing and by setting it up wiht a hashmap was able to figure out how to optimize it. 

## What I Learned

- Strings can be sorted. Also learned that you can set a default value with get() instead of just having nothing such as get(value, 0).
