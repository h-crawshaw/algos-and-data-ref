def findMaxArea(heights):
  l, r = 0, len(heights) - 1
  max_area = 0

  while l < r:
    current_area = min(heights[l], heights[r]) * (r - l)
    max_area = max(max_area, current_area)
    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1
  return max_area
