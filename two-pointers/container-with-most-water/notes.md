# Container With Most Water — Notes

## First Thoughts

I needed to compare two heights and calculate how much water they could hold. The important part was realizing that the width between the heights also matters, not just the tallest lines.

## Independent Attempt

- **Attempt time:** 20 minutes

## Brute-Force Approach

A brute-force approach would check every possible pair of heights and calculate the area for each pair.

This works logically, but it repeats too much work because every height gets compared with every other height.

## Optimized Approach

The optimized approach uses two pointers. One pointer starts at the beginning and one starts at the end.

At each step, I calculate the area using the shorter height and the current width. Then I move the pointer that has the smaller height, because moving the taller height would not help if the shorter height is still limiting the area.

When both heights are equal, moving either pointer is correct. I used `<=` so the left pointer moves when the heights are equal.

- **Data structure / pattern:**
Two pointers

- **Time complexity:**
O(n)

- **Space complexity:**
O(1)

## Mistakes and Debugging

- I had to understand that the shorter height controls the water level.
- I learned that equal-height cases can move either pointer.
- I noticed that small runtime changes on LeetCode can just be random noise even when the algorithm is the same.

## What I Learned

- Two pointers work well when I can safely eliminate one side each step.
- The area is calculated with the smaller height times the width.
- Same big-O solutions can have slightly different runtime because of constant work and platform randomness.
