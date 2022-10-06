# Time: O(logn)
# Space: O(1)

nums = [1, 2, 4, 6, 7, 11, 14, 15, 17, 20]
target = 14

def BinSearch(nums, target):
  l, r = 0, len(nums) - 1

  while l <= r:
    mid = l + (r - l) // 2

    if target > nums[mid]:
      l = mid + 1
    elif target < nums[mid]:
      r = mid - 1
    else:
      return mid
  return -1