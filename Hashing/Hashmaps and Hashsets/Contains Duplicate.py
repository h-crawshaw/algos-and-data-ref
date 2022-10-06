# Time: O(n)
# Space: O(n)

nums = [1, 2, 4, 5, 2]

def containsDuplicate(nums):
  hashset = set()

  for n in nums:
    if n in hashset:
      return True
    hashset.add(n)
  return False