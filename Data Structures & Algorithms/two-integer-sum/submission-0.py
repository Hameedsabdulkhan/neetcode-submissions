from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,nums in enumerate(nums):
            difference=target-nums
            if difference in hash_map:
                return [hash_map[difference],i]
            hash_map[nums]=i
