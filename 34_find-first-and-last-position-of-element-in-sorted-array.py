from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)-1
        return [self.st_pos(nums, target, lo, hi),self.en_pos(nums, target, lo, hi)]

    def st_pos(self, nums, target, lo, hi):
        lo, hi = 0, len(nums) - 1
        first_pos = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
            if target == nums[mid]:
                first_pos = mid  
        return first_pos
    
    def en_pos(self, nums, target, lo, hi):
        lo, hi = 0, len(nums) - 1
        last_pos = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
            if target == nums[mid]:
                last_pos = mid  
        return last_pos

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10],8))
