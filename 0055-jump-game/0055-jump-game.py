class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i>max_reach:
                return False
            
            reach = i+nums[i]

            if reach>max_reach:
                max_reach = reach
            
            if max_reach >= last:
                return True
        return False