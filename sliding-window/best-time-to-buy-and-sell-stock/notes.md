# Best Time to Buy and Sell Stock — Notes

## First Thoughts

I needed to keep track of the lowest price seen so far and compare every current price against that low price.

## Independent Attempt

- **Attempt time:** 15 minutes

## Brute-Force Approach

A brute-force approach would try every possible buy day and every possible sell day after it. Then it would calculate the profit for each pair.

This works logically, but it repeats too much work because every day gets compared with many other days.

## Optimized Approach

The optimized solution keeps one variable for the lowest price seen so far and one variable for the best profit so far.

For every price, I update the current lowest price first. Then I check how much profit I could make if I sold at the current price. If that profit is better than the best profit, I update the answer.

- **Data structure / pattern:**
Sliding window / running minimum

- **Time complexity:**
O(n)

- **Space complexity:**
O(1)

## Mistakes and Debugging

- I had to remember that the buy day must come before the sell day.
- I learned that I do not need to store every possible pair.
- Tracking the current lowest price is enough to know the best buy point so far.

## What I Learned

- A running minimum can replace nested loops.
- For stock profit problems, the current price can be treated as the sell price while the lowest previous price is the buy price.
- If prices only decrease, the answer should stay at 0.
