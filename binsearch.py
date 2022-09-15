def binsearch(arr,target):

    low = 0
    high = len(arr)

    while high >= low:
      middle = (high+low)//2

      if arr[middle] < target:
         low = middle +1

      elif arr[middle] > target:
         high = middle -1

      else:
         return middle
  
    return -1


print(binsearch([3,6,16,23,37,50,52],52))

