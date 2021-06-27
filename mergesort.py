#Algorthm and implemtation of Merge Sort
"""
MergeSort(arr[], l, r)
if l < r
  1. Find the middle point to divide the array into two halves:
    middle m = l + (r - l)/ 2

  2. Call MergeSort for first half:
        MergeSort(arr, l , m)

  3. Call mergeSort for second half:
        MergeSort(arr, m + 1, r)

  4. Merge the two halves sorted in step 2 and step 3:
       merge(arr, l , m , r)
"""

def merge(arr, L , mid, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j] :
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        merge(arr , L , mid , R)

def printSort(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

arr = [8, 3, 9, 5, 2, 6]

mergeSort(arr)
printSort(arr)


#Time and Space Complexity of merge sort algorithm is
"""
Time Complexity
  Best case : Ω(n log(n))
  Avergae case : Θ(n log(n))
  Worst case : O(n log(n))

Space Complexity
  Worst case : O(n)
"""
