//Algorthm and implementation of Bubble Sort
/*
  bubbleSort A

  for i = 0 to A.length - 1

    for j = 0 to A.length - 1 - i

      if A[j] > A[j + 1]
        temp = A[j]
        A[j] = A[j + 1]
        A[j + 1] = temp

*/

#include<stdio.h>
#include<stdlib.h>

void bubbleSort(int arr[], int n){
  int i , j;
  for(i = 0; i < n - 1; i++)
    for(j = 0; j < n - i - 1; j++)
      if( arr[j] > arr[j + 1] ){
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
      }
}

void printSort(int arr[],int n){
    for(int i = 0; i < n; i++)
      printf("%d ", arr[i]);
}

void main(){
  int arr[] = {9,3,5,2,0,1};
  int n = sizeof(arr) / sizeof(arr[0]);

  bubbleSort(arr, n);
  printSort(arr, n);
}


//Time and Space Complexity of bubble sort algorithm is
/*
Time analysis
  Best case : Ω(n)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)
*/
