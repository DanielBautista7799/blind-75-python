# Encode and Decode Strings — Notes

## First Thoughts

I needed a way to combine strings without losing where one string ends and the next begins. I used the length of each word as a prefix, followed by a separator, then the word itself.

## Independent Attempt

- **Attempt time:** 60 minutes

## Brute-Force Approach

A weak approach would be joining strings with a normal separator like # or ,. That breaks if the original strings already contain the separator.

## Optimized Approach

I encoded each string as its length, then a #, then the string. During decode, I read the length first, skip the #, then read exactly that many characters.

- **Data structure / pattern:**
String parsing

- **Time complexity:**
O(n)

- **Space complexity:**
O(n)

## Mistakes and Debugging

- I had to make sure the decoder reads the length first instead of splitting on #. I needed to move through the string carefully after reading each word. The separator is safe because the decoder uses the length to know exactly how many characters belong to the word.

## What I Learned

- Length-prefix encoding avoids separator conflicts. When decoding strings, using indexes and slicing carefully matters.  A delimiter alone is not always safe if the input can contain that delimiter.
