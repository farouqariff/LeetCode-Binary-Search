class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak():
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search_left(target, left, right):
            while left <= right:
                mid = (left + right) // 2
                value = mountain_arr.get(mid)
                if value == target:
                    return mid
                elif value < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def binary_search_right(target, left, right):
            while left <= right:
                mid = (left + right) // 2
                value = mountain_arr.get(mid)
                if value == target:
                    return mid
                elif value > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        n = mountain_arr.length()
        peak = find_peak()

        left_result = binary_search_left(target, 0, peak)
        if left_result != -1:
            return left_result

        return binary_search_right(target, peak + 1, n - 1)
    
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.calls = 0

    def get(self, index):
        if index < 0 or index >= len(self.arr):
            raise IndexError("Index out of bounds")
        self.calls += 1
        return self.arr[index]

    def length(self):
        return len(self.arr)

mountain_arr = MountainArray([1,2,3,4,5,3,1])
solution = Solution()
target = 3
print(solution.findInMountainArray(target, mountain_arr))