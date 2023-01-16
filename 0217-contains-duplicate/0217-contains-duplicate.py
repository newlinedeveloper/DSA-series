class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()
        
        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        
        # return False
        
        hash = {}

        for i in nums:
            if i in hash.keys():
                return True
            hash[i] = hash.get(i,0)+1
        return False
        