#Algorthm and implementation of Bubble Sort
"""
  bubbleSort A

  for i = 0 to A.length - 1

    for j = 0 to A.length - 1 - i

      if A[j] > A[j + 1]
        temp = A[j]
        A[j] = A[j + 1]
        A[j + 1] = temp

"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def printSort(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

arr = [9, 2, 8, 3, 7, 4, 5]

bubbleSort(arr)
printSort(arr)


#Time and Space Complexity of bubble sort algorithm is
"""
Time analysis
  Best case : Ω(n)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)
"""
