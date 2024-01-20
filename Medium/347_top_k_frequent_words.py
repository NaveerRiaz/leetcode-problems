class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for key, value in counts.items():
            frequency[value].append(key)

        k_sorted = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                k_sorted.append(j)
                if len(k_sorted) == k:
                    return k_sorted
