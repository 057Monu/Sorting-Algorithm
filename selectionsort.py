#Algorithm and implementation for Selection sort
"""
SelectionSort A
  for i = 1 to A.length - 1
    min = i
    for j = i + 1 to A.length
      if A[j] < A[min]
        min = j

    temp = A[i]
    A[i] = A[min]
    A[min] = temp

"""

def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

def printSort(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

arr = [9, 2, 8, 3, 7, 4, 6, 5]

selectionSort(arr)
printSort(arr)


#Time and Space Complexity of selection sort algorithm is
"""
Time Complexity
  Best case : Ω(n^2)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)

"""
