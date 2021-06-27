//Algorithm and implementation for Selection sort
/*
SelectionSort A
  for i = 1 to A.length - 1
    min = i
    for j = i + 1 to A.length
      if A[j] < A[min]
        min = j

    temp = A[i]
    A[i] = A[min]
    A[min] = temp

*/

public class SelectionSort {

  void sort(int arr[], int n){
    for(int i = 0; i < n - 1; i++){
      int min = i;
      for(int j = i + 1; j < n; j++)
        if(arr[j] < arr[min])
          min = j;

      int temp = arr[i];
      arr[i] = arr[min];
      arr[min] = temp;
    }
  }

  static void printSort(int arr[], int n){
    for(int i = 0; i < n; i++)
      System.out.print(arr[i] + " ");
  }

  public static void main(String[] args){
    int arr[] = {9, 2, 8, 3, 7, 4, 6, 5};
    int n = arr.length;

    SelectionSort selection = new SelectionSort();
    selection.sort(arr,n);

    printSort(arr, n);
  }
}


//Time and Space Complexity of selection sort algorithm is
/*
Time Complexity
  Best case : Ω(n^2)
  Avergae case : Θ(n^2)
  Worst case : O(n^2)

Space Complexity
  Worst case : O(1)
*/
