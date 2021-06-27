//Algorithm for insertion sort

/* InsertionSort A
for j = 2 to A.length
key = A[j]
i = j - 1
while ((i > 0) and (A[i] > key){
  A[i + 1] = A[i]
  i = i - 1
}
A[i + 1] = key

*/

//Code for the above algorthm for insertion sort
public class Insertionsort {
  void sort(int arr[], int n){
    for(int j = 1; j < n; j++){
      int key = arr[j];
      int i = j - 1;

      while(i >= 0 && arr[i] > key){
        arr[i + 1] = arr[i];
        i = i - 1;
      }
      arr[i + 1] = key;
    }
  }

static void printSort(int arr[], int n){
    for(int i = 0; i < n; i++)
      System.out.print(arr[i] + " ");
}

public static void main(String[] args){
  int arr[] = { 9, 7, 2, 6, 8, 5};
  int n = arr.length;
  Insertionsort insertion = new Insertionsort();
  insertion.sort(arr, n);

  printSort(arr, n);
  }
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
