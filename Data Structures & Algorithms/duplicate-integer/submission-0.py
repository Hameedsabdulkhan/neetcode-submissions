from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map=defaultdict(int)
        for i in nums:
            if hash_map[i]>=1:
                return True
            else :
                hash_map[i]+=1
        return False
            
