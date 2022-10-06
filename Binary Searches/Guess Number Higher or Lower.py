def guessNumber(self, n: int) -> int:
  l, r = 1, n
  
  while l <= r:
    mid = (l + r) // 2
    if guess(mid) == -1:
      r = mid - 1
    elif guess(mid) == 1:
      l = mid + 1
    else:
      return mid