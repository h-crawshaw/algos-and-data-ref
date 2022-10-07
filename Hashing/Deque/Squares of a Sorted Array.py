import collections
def sortSquares(nums):
  res = collections.deque()
  l, r = 0, len(nums) - 1

  while l <= r:
    lval, rval = abs(nums[l]), abs(nums[r])
    if lval > rval:
      res.appendleft(lval*lval)
      l += 1
    else:
      res.appendleft(rval*rval)
      r -= 1
  return list(res)

nums = [-4,-1,0,3,10]
print(sortSquares(nums))