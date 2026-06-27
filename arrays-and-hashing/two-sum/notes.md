# Two Sum — Notes

## First Thoughts

Initially I completed it like it was an ordered two sum problem, but then realized it could be in any order so the approach has to be different. Obviously we are going to incorporate hashing somehow but right now im unsure of where. Lastly, we need to set the bounds of i and j correctly.

## Independent Attempt

- **Attempt time:** 25 minutes

## Brute-Force Approach

The brute force solution wasn't done but I am assuming it would consist of iterating through every number and doing an iteration through the whole list which would take a considerable amount of time.

## Optimized Approach

The optimized apporach saved the seen numbers in a hash map with the indexes as their values. The current number needed to reach the target was seen it would be found immediately in the hash map at which time I could return the value of the seen hashmap and the current index to give the correct answer.

- **Data structure / pattern:**Hashmap
- **Time complexity:**0(n)
- **Space complexity:**0(1)

## Mistakes and Debugging

- Mistakes I made debugging include  i =+1  which is just i is a positive 1 and also iterating through all of seen when i can just use the in key word for finding key values.

## What I Learned

-I learned that it is much quicker to save what you need in the case of iteration and later on calling back on it as fast as possible using a hashmap save a lot of time.
