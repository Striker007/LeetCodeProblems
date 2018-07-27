class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = {}
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in checked:
                return [checked[comp], i]
            checked[nums[i]] = i

        return None
