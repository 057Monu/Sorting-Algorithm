//Algorthm and implemtation of Merge Sort
/*
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
*/

#include<stdio.h>
#include<stdlib.h>

void merge(int arr[], int l , int m , int r){
  int i , j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  int L[n1], R[n2];

  for(i = 0; i < n1; i++)
    L[i] = arr[l + i];
  for(j = 0; j < n2; j++)
    R[j] = arr[m + 1 + j];

  i = 0; j = 0; k = l;
  while(i < n1 && j < n2){
    if(L[i] <= R[j]){
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }
  while( i < n1){
    arr[k] = L[i];
    i++;
    k++;
  }
  while( j < n2){
    arr[k] = R[j];
    j++;
    k++;
  }
}

void mergeSort(int arr[], int l, int r){
    if(l < r){
      int m = l + (r - l) / 2;

      mergeSort(arr, l , m);
      mergeSort(arr, m + 1, r);

      merge(arr, l , m , r);
    }
}

void printSort(int arr[], int n){
    for(int i = 0; i < n; i++)
      printf("%d ", arr[i]);
}

int main(){
  int arr[] = {6,3,8,2,9,1};
  int n = sizeof(arr) / sizeof(arr[0]);

  mergeSort(arr, 0 , n - 1);
  printSort(arr, n);
  return 0;
}


//Time and Space Complexity of merge sort algorithm is
/*
Time Complexity
  Best case : Ω(n log(n))
  Avergae case : Θ(n log(n))
  Worst case : O(n log(n))

Space Complexity
  Worst case : O(n)
*/
