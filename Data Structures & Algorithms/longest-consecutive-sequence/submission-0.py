class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumsSet=set(nums)
        longest=0
        for n in nums:
            if n-1 not in NumsSet:
                length=0
                while (n+length) in NumsSet:
                    length+=1
                    longest=max(length,longest)
        return longest


