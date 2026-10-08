class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums.sort()
        print(nums)
        #for i in range(len(nums)-1):
         #   if nums[i]==nums[i+1]:
          #      return True
        #return False
        s=set(nums)
        if len(s)==len(nums):
            return False
        return True

        