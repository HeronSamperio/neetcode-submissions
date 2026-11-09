class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)<=0): return False
        temp = {nums[0]}
        for i in nums[1::1]:
            if i in temp:
                return True
            temp.add(i)
        return False
