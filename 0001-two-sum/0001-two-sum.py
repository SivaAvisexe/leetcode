class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       arr = {}
       t=0
       for i,n in enumerate(nums):
        t=target - n
        if t in arr.keys():
            return [arr[t],i]
        else:
            arr[n]=i
            

