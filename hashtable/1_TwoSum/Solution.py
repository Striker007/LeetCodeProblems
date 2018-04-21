class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {nums[i]: i for i in range(0, len(nums))}
        for i in range(0, len(nums)):
            compl = target - nums[i]
            if compl in numsMap and numsMap[compl] != i:
                return (i, numsMap[compl])
