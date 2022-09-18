#binsearch
#Richard Parker
#CSCI 77800 Fall 2022
#collaborators: none
#consulted: none



def binsearch (arr, target):

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

a = binsearch ([3,6,16,23,37,50,52], 23)

print("Target found at index " + str(a) if a>0 else "Target not found")

