class Solution:
    def moveZeroes(nums):
        for i in nums:
            if i<=0:
                nums.append(i)
        return nums        

 