# Time: O(n^2)
# Space: O(n)

target = 13
nums = [2, 7, 11 ,15]

def twoSum(target, nums):
  hashmap = {}

  for i, n in enumerate(nums):
    difference = target - n
    if difference in hashmap:
      return [hashmap[difference], i]
    hashmap[n] = i