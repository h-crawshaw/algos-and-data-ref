
nums = [12, 4, 5, 6, 7, 3, 1, 15]

def quicksort(array):
  if len(array) < 2:
    return array

  else:
    pivot = array[0]
    lesser = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort(nums))