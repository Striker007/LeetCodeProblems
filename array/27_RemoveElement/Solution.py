class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        step = 0
        try:
            while True:
                if nums[step] == val:
                    del(nums[step])
                    if step > 0:
                        step -= 1
                else:
                    step += 1
        except IndexError as e:
            pass

        return len(nums)
                