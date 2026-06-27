"""Solution for LeetCode 347: Top K Frequent Elements."""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        array = []

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for _ in range(k):
            bestvalue = 0
            bestnum = None

            for num in hashmap:
                if hashmap[num] > bestvalue:
                    bestvalue = hashmap[num]
                    bestnum = num

            array.append(bestnum)
            hashmap.pop(bestnum)

        return array
