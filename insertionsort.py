#Algorithm for insertion sort
"""
 InsertionSort A
for j = 2 to A.length
key = A[j]
i = j - 1

while ((i > 0) and (A[i] > key){
  A[i + 1] = A[i]
  i = i - 1
}
A[i + 1] = key
"""

#Code for the above algorthm for insertion sort
def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key :
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

def printSort(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

arr = [9, 3, 8, 2, 4, 1]
insertionSort(arr)
printSort(arr)


#Time and Space Complexity of insertion sort algorithm is
"""
Time Complexity
  Best case : Ω(n)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)
"""
