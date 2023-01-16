class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i,n in enumerate(nums):
            diff =  target - n
            if diff in hash.keys():
                return [hash[diff],i]
            hash[n] = i 
            
        