from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = Solution.bubble_sort(nums)


    @staticmethod
    def bubble_sort(arr):
        # Outer loop to iterate through the list n times
        for n in range(len(arr) - 1, 0, -1):
            # Initialize swapped to track if any swaps occur
            swapped = False  
            # Inner loop to compare adjacent elements
            for i in range(n):
                if arr[i] > arr[i + 1]:
                    # Swap elements if they are in the wrong order
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    # Mark that a swap has occurred
                    swapped = True
            # If no swaps occurred, the list is already sorted
            if not swapped:
                break
        return arr