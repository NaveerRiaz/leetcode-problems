class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hmap.keys():
                return [i, hmap.get(rem)]
            hmap[nums[i]] = i
