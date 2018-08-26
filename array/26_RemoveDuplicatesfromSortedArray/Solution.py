class Solution:
    def removeDuplicates(self, nums):
        s = Solution3()
        return s.removeDuplicates(nums)


class Solution1:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        # when len >= 2
        curr_index = 1
        prev = nums[0]

        for i in nums[1:]:
            if i == prev:
                del nums[curr_index]
            else:
                prev = i
                curr_index += 1

        return curr_index


 class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)

        curr_index = 1
        prev = nums[0]
        for i in nums[1:]:
            if i == prev:
                del nums[curr_index]
            else:
                prev = i
                curr_index += 1

        return curr_index

        
 class Solution3:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)

        curr_index = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[curr_index] = nums[i]
                curr_index += 1
            prev = nums[i]

        return curr_index


class Solution4:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)

        curr_index = 1
        prev = nums[0]
        for i in nums[1:]:
            if i != prev:
                nums[curr_index] = i
                curr_index += 1
            prev = i

        return curr_index
