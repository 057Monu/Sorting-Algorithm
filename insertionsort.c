//Algorithm for insertion sort

/* InsertionSort A
for j = 2 to A.length
key = A[j]
i = j - 1
while ((i > 0) and (A[i] > key)
  A[i + 1] = A[i]
  i = i - 1

A[i + 1] = key

*/

//Code for the above algorthm for insertion sort
#include<stdio.h>
void insertionSort(int A[], int n){
  for(int j = 1; j < n; j++){
    int key = A[i];
    int i = j - 1;
    while( (i >= 0) && (A[i] > key)){
      A[i + 1] = A[i];
      i = i - 1;
    }
    A[i + 1] = key;
  }
}

void printSort(int arr[], int n){
  for(int i = 0; i < n; i++){
    printf("%d ", arr[i]);
  }
}

int main(){

  int n = 5;
  int arr[] = {13,11,3,10,6};

  insertionSort(arr, n);
  printSort(arr,n);
  return 0;
}

//Time and Space Complexity of insertion sort algorithm is
/*
Time Complexity
  Best case : Ω(n)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)
*/
