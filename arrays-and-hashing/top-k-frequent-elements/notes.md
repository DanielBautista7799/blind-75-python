# Top K Frequent Elements — Notes

## First Thoughts

I knew I needed to count how many times each number appeared first. I started by using a hashmap to store each number and its frequency.

## Independent Attempt

- **Attempt time:** 45 minutes

## Brute-Force Approach

A brute-force approach would repeatedly count or search through the list to find the most common values. This would be slower because it would keep scanning the same numbers again.

## Optimized Approach

I used a hashmap to count the frequency of each number. Then I repeated the process k times: find the number with the highest remaining frequency, add it to the answer, and remove it from the hashmap so it would not be chosen again.

- **Data structure / pattern:** Hashmap
- **Time complexity:**O(n)
- **Space complexity:**O(n)
## Mistakes and Debugging
I mixed up looping through values versus looping through indexes. I initially tried to get the key from the max value directly I forgot that bestvalue` and bestnum need to reset every time I search for the next most frequent number.

## What I Learned
When looping through a dictionary, the loop variable is the key. To find the key with the highest value, I need to compare the values but save the key.
