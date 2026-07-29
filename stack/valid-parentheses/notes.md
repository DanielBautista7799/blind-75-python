# Valid Parentheses — Notes

## First Thoughts

My first thought was to use a stack. Every opening bracket gets pushed onto the stack, and every closing bracket should match the most recent opening bracket.

## Independent Attempt

- **Attempt time:** 20 minutes

## Brute-Force Approach

I could try checking every bracket against the rest of the string until I found its match, but that would get really messy once nested brackets are involved.

## Optimized Approach

The stack makes this problem pretty straightforward. Whenever I see an opening bracket I save it. When I see a closing bracket, I pop the last opening bracket off the stack and use the dictionary to see if they match.

If they don't match, or if the stack is already empty, I know the string is invalid immediately.

At the end I return `stack == []` because if anything is left in the stack, those brackets never found a match.

- **Data structure / pattern:** Stack
- **Time complexity:** O(n)
- **Space complexity:** O(n)

## Mistakes and Debugging

- I had to make sure I didn't pop from an empty stack.
- I also needed to remember to check if the stack was empty after processing the whole string.

## What I Learned

- Stacks are really useful whenever the last thing added is the first thing I need to use.
- Using a dictionary for matching brackets is much cleaner than a bunch of if statements.
