# Group Anagrams — Notes

## First Thoughts
Initial thoughts consisted of creating a counter similar to leetcode anagrams which would have counter which would be used to compare itself against other strs to add them to a tuple.

## Independent Attempt

- **Attempt time:** 40 minutes

## Brute-Force Approach

Im not really sure what the brute force approach for this problem would be. I could potentially run through each word and add it to a list if the sorted word was the same as the next word and so on but that seems very inefficent and a lot harder to implement.

## Optimized Approach

This appraoch works but using the counter from anagrams multiple times and keeping the count as a key for future words. By keeping a count for a word we get a grouping such as ("c":1,"a":1,"t":1 ) to tell us the characters in a word. An anagram has the same ammount of letters in it to work so to make sure it was able to be used later in comparison to other words it has to be made into a key. By sorting the list and then making it a tuple it allows us to use it as a dictonary key. It is then added to groups with the sorted key as its key and the word as its value. If seen again the key will add the word currently on to the key or create a new subset with a new key. Lastly we return the value of groups so we can see all groupings of words without their keys.

- **Data structure / pattern:** Hashmaps
- **Time complexity:** O(m+n)
- **Space complexity:** O(m)

## Mistakes and Debugging

-I initally tried to make multiple arrays with their own counts but the difficulty was that I wasn't sure how to use the count for other words. I had to research how to may a larger key which allowed me to do so and by doing that I figured out you can use tuples as keys.

## What I Learned

-You can make a hashable object from a tuple. 
