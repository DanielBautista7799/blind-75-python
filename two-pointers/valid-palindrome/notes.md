# Valid Palindrome — Notes

## First Thoughts

I knew I needed to compare the string forward and backward, but the main issue was cleaning the string first. The problem ignores spaces, punctuation, and capitalization.

## Independent Attempt

- **Attempt time:** 20 minutes

## Brute-Force Approach

My approach was to build a cleaned version of the string first. I looped through every character, kept only letters and numbers, converted everything to lowercase, and then compared the cleaned string with its reverse.

## Optimized Approach

The solution uses `isalnum()` to check whether a character is alphanumeric. That means the character is either a letter or a number.

After creating the cleaned string, I compare it to the reversed version of itself. If both are the same, then the original string is a valid palindrome after cleaning.

- **Data structure / pattern:**
String cleaning

- **Time complexity:**
O(n)

- **Space complexity:**
O(n)

## Mistakes and Debugging

- I did not know about the `isalnum()` function at first.
- I had to understand that punctuation and spaces should be ignored completely.
- I learned that reversing a string with slicing creates the reverse copy.

## What I Learned

- `char.isalnum()` returns `True` if `char` is a letter or number.
- `clean[::-1]` returns the reversed version of the string.
- Some palindrome problems are more about cleaning the input correctly than the comparison itself.
