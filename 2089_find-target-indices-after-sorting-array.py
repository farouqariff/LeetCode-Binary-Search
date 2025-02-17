from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = self.quicksort(nums[:])

        start = self.find_start(sorted_nums, target)
        end = self.find_end(sorted_nums, target)

        if start == -1:
            return []
        
        return list(range(start, end + 1))

    def find_start(self, sorted_nums, target):
        lo, hi = 0, len(sorted_nums)-1
        start = -1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if target > sorted_nums[mid]:
                lo = mid + 1
            elif target < sorted_nums[mid]:
                hi = mid - 1
            else:
                start = mid
                hi = mid - 1
        return start

    def find_end(self, sorted_nums, target):
        lo, hi = 0, len(sorted_nums) - 1
        end = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > sorted_nums[mid]:
                lo = mid + 1
            elif target < sorted_nums[mid]:
                hi = mid - 1
            else:
                end = mid
                lo = mid + 1
        return end

    def quicksort(self, array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quicksort(array, low, pivot_index - 1)
            self.quicksort(array, pivot_index + 1, high)
        
        return array

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i+1
