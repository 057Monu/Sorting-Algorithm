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

public class BubbleSort {

  void sort(int arr[], int n){

  for(int i = 0; i < n; i++)
    for(int j = 0; j < n - i - 1; j++)
      if( arr[j] > arr[j + 1]) {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
  }
}

static void printSort(int arr[], int n){
    for(int i = 0; i < n; i++)
      System.out.print(arr[i] + " ");
}

  public static void main(String[] args){
    int arr[] = {9 , 5, 8, 2, 7, 3};
    int n = arr.length;

    BubbleSort bubble = new BubbleSort();
    bubble.sort(arr, n);

    printSort(arr, n);
  }
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
