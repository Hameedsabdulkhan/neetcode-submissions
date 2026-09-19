class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_maps={}
        hash_mapt={}
        for i in s:
            if i in hash_maps:
              hash_maps[i]+=1
            else:
              hash_maps[i]=1
              
        for i in t:
            if i in hash_mapt:
                hash_mapt[i]+=1
            else:
                hash_mapt[i]=1
        if hash_maps==hash_mapt:
            return True
        else:
            return False