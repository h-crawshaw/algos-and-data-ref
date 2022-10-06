from pandas import array


mnt = [2, 4, 5, 9, 6, 5, 4, 2, 1]

def peakIndex(mnt):
  l, r = 0, len(mnt) - 1

  while l <= r:
    mid = (l + r) // 2
    if mnt[mid - 1] < mnt[mid] > mnt[mid + 1]:
      return mid
    elif mnt[mid - 1] < mnt[mid]:
      l = mid + 1
    else:
      r = mid