class Solution:
    def rotate_list_search_minimum(self, nums: list):
        if len(nums) <= 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            if nums[left] <= nums[right]:
                return nums[left]
            else:
                mid = (left + right) // 2
                if nums[mid] <= nums[left]:
                    right = mid
                else:
                    left = mid + 1
        return min(nums[left], nums[right])

    def rotate_list_search_target(self, nums: list, target: int):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    # search in left
                else:
                    # search in right
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    # search in right
                    left = mid + 1
                else:
                    # search in left
                    right = mid - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
