# inputs are a list of nums
# If array has dups, return true
# if array doesn't, return false

# put array into a set  dups
# compare length of both lists
# if lists length not equal, return true
# else return false



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        copy = set(nums)
        if len(nums) == len(copy):
            return False
        else:
            return True