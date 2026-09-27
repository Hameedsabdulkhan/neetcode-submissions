from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        
        for val, freq in counter.items():
            buckets[freq].append(val)  
            
        collected = []
        
        
        for i in range(n, -1, -1):
            for num in buckets[i]:
                collected.append(num)
                
                if len(collected) == k:
                    return collected
