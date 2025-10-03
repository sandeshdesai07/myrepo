class Solution:
    def moveZeroes(nums):
        for i in nums:
            if i<=0:
                nums.append(i)
        return nums        

    moveZeroes([1,0,3,4,5,0])        