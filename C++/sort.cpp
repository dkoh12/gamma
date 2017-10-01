#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

void print(int a[], int sz) {
	for(int i=0; i<sz; i++) {
		cout << a[i] << " ";
	}
	cout << endl;
}


void swap(int &x, int &y) {
	int temp = x;
	x = y;
	y = temp;


	// THE FOLLOWING DOES NOT WORK IF YOU TRY TO SWAP THE SAME ELEMENTS!!
	// THEY CANCEL EACH OTHER OUT!!
	// x = x ^ y;
	// y = x ^ y;
	// x = x ^ y;

	// int temp = *(a+j+1);
	// *(a+j+1) = *(a+j);
	// *(a+j) = temp;
}


// http://www.bogotobogo.com/Algorithms/insertionsort.php
/*
 ===========================
		Bubble Sort
 ===========================
O(n^2)
*/

void BubbleSort(int *a, int size) {
	for (int i=0; i<size-1; i++) {
		for (int j=0; j<size-1; j++) {
			if (*(a+j) > *(a+j+1)) {
				// swap
				swap(*(a+j), *(a+j+1));
			}
		}
		// uncomment to see 
		print(a, size);
	}
}

void executeBubbleSort() {
	int a[] = {5, 7, 1, 3, 4, 9, 2, 6, 8, 0};
	const size_t sz = sizeof(a)/sizeof(a[0]);

	print(a, sz);

	cout << "===================" << endl;
	BubbleSort(a, sz);
}

/*
 =================================================
		Insertion Sort (Way we sort a card deck)
 =================================================

efficient for small & mostly sorted lists 
O(n+d) where d = # of inversions
insertion is expensive since you have to shift all following elemnts by 1

stable sort. (does not change relative order of elements)
in-place sort.

2 subarrays: 1 sorted, another unsorted.

From unsorted array take first element and put it in right place in sorted array

*/

void insertion(int a[], int sz){
	for (int i=1; i<sz; i++) {
		int j=i;

		while(j>0 && (a[j] < a[j-1])) {
			swap(a[j], a[j-1]);
			j--;
		}
		// uncomment to see
		cout << endl;
		for (int k=0; k<sz; k++) cout << setw(3) << a[k]; //setw(x) == spacing
	}
}

void executeInsertionSort() {
	int a[] = { 15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14};
	int size = sizeof(a)/sizeof(int);
	for (int i = 0; i < size; i++) cout << setw(3) << a[i];
	insertion(a, size);
	cout << endl;
}

/*
 =================================================
		Shell Sort (Way we sort a card deck)
 =================================================
Generalization of Insertion Sort
but works better on larger lists

compare elements far apart then use insertion sort on almost sorted array

O(n^2)
*/

void shellSort(int arr[], int n) {
	for(int gap=n/2; gap>0; gap/=2) {
		// for all elements to right of gap
		for(int i=gap; i<n; i++) {
			int temp = arr[i];
			int j;
			// continue shifting elements until correct location for a[i] is found
			for(j=i; j>=gap && arr[j-gap] > temp; j -= gap) {
				arr[j] = arr[j-gap];
			}
			arr[j] = temp;


			print(arr, n);
		}

		cout << "GAP" << endl;
	}
}

void executeShellSort() {
	int arr[] = {12, 34, 54, 2, 3};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    cout << "Array before sorting: \n";
    print(arr, n);
    shellSort(arr, n);
    cout << "Array after sorting: \n";
    print(arr, n);
}


/*
 =============================
		Selection Sort
 =============================
O(n^2). in place comparison.. Slowest of all sorting alg
Maintains 2 subarray. One sorted. Other unsorted.

From unsorted array take smallest element, and append it to sorted list.

*/

void selectionSort(int arr[], int n) {
	for(int i=0; i < n-1; i++) {
		int min_idx = i;

		for(int j=i+1; j < n; j++) {
			if (arr[j] < arr[min_idx]) 
				min_idx = j;
		}
		swap(arr[min_idx], arr[i]);
		print(arr, n);
	}
}

void executeSelectionSort() {
	int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    print(arr, n);
    selectionSort(arr, n);
}


/*
 =============================
		Counting Sort   (Non comparison)
 =============================
Sort n elements but all are in range 0-k where k is much smaller than n.

Create k buckets that store # of times kth element was seen in array.
Process count values in ordering provided by k buckets


O(n+k) where n = size of array, k = size of range

*/

void CountingSort(int arr[], int sz){
	int i, j, k, min, max;
	int idx=0;

	min = max = arr[0];
	for(i=1;i<sz;i++) {
		min = (arr[i] < min) ? arr[i] : min;
		max = (arr[i] > max) ? arr[i] : max;
	}

	k = max-min+1;
	// create k buckets
	//int *B = new int[k];
	//for(i=0;i<k;i++) B[i]=0;
	int *B = (int *) calloc(k, sizeof(int));
	for(i=0;i<sz;i++) 
		B[arr[i]-min]++;

	cout << "counts" << endl;
	print(B, k);
	cout << "array" << endl;
	// print(arr, sz);

	for(i = min;i <= max;i++) {
		for(j = 0; j < B[i-min]; j++) {
			arr[idx++] = i;
		}
		// cout << "i " << i << " j " << j << endl;
		print(arr, sz);
	}


	print(arr, sz);
	delete[] B;

}


void executeCountingSort() {
	int a[] = {5,9,3,9,10,9,2,4,13,10};
	const size_t sz = sizeof(a)/sizeof(a[0]);
	print(a,sz);
	cout << "----------------------\n" ;
	CountingSort(a, sz);
}


/*
 =============================
		Radix Sort   (Non comparison)
 =============================
radix = position in a number.
42 has 2 radices: 4, 2.
in hex, 0xAB has 2 radices: A, B

LSD - Least Significant Digit
MSD - Most Significant Digit

if range is from 1 to n^2, counting sort will take O(n^2)
radix sort will take O(n) (digit by digit sorting)

radix sort uses counting sort as a subroutine

O(d*(n+b)) 
where b = base of number (ie. 2, 10)
d = O(log_b (k)) where k is max possible value

O((n+b) * log_b(k))
for large k -> O(n log_b n)
if b is large -> we get O(n)
*/

const int MAX=10;

void RadixSortLSD(int *a, int sz) {
	int i, bucket[sz], maxVal =0, digitPosition=1;
	
	// get max val in arr[]
	for(i=0;i<sz; i++) {
		if(a[i] > maxVal)
			maxVal = a[i];
	}

	int pass =1;
	while(maxVal/digitPosition > 0) {
		int * digitCount = (int*) calloc(10, sizeof(int));
		// int digitCount[10] = {0};

		// store count of occurences in count[]
		for(i=0;i<sz;i++)
			digitCount[(a[i]/digitPosition)%10]++;

		// change count[i] so that it now contains actual position of this digit in output
		for(i=1;i<10;i++)
			digitCount[i] += digitCount[i-1];

		// build output array (MAGIC happens here)
		for(i=sz-1;i>=0;i--) {
			//cout << "digitCount" << endl;
			//print(digitCount, MAX);
			//cout << digitCount[(a[i]/digitPosition)%10] << endl;
			//cout << a[i] << endl;
			bucket[--digitCount[(a[i]/digitPosition)%10]] = a[i];

			//cout << "bucket" << endl;
			//print(bucket, sz);
		}

		// copy output array to arr[]
		for(i=0;i<sz;i++)
			a[i] = bucket[i];

		cout << "pass #" << pass++ << ": ";
		print(a, sz);

		digitPosition *= 10;

	}
}

void executeRadixSort(){
	int a[] = {170, 45, 75, 90, 2, 24, 802, 66};
	const size_t sz = sizeof(a)/sizeof(a[0]);

	cout << "pass #0: ";
	print(a,sz);
	RadixSortLSD(a,sz);
}


/*
 =============================
		Bucket Sort    (Non comparison)
 =============================
O(n)

can be used with keys that are floating point numbers unlike Counting Sort which need keys that are indices

Create n buckets O(n)
For each element put it in bucket[n*arr[i]] O(n)
sort individual buckets using insertion sort (also takes O(n))
concat all sorted buckets O(n)

*/

void bucketSort(float arr[], int n){
	// create n buckets
	std::vector<float> b[n];

	// put array elem in diff buckets
	for(int i=0; i<n; i++) {
		int j = n*arr[i]; // index in bucket
		b[j].push_back(arr[i]);
	}

	// sort individual buckets w/ insertion sort
	for(int i=0;i<n;i++) {
		sort(b[i].begin(), b[i].end()); // I believe this is insertion sort
	}

	// concat all buckets into arr[]
	int index = 0;
	for(int i=0; i<n;i++) {
		for(int j=0; j <b[i].size(); j++) {
			arr[index++] = b[i][j];
		}
	}
}


void print(float arr[], int n) {
	for(int i=0; i<n; i++) {
		cout << arr[i] <<" ";
	}
	cout << endl;
}

void executeBucketSort() {
	float arr[] = {0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<< "before sort" << endl;
    print(arr, n);
    bucketSort(arr, n);
    cout << "after sort" << endl;
    print(arr, n);
}


/*
 =============================
		Quick Sort
 =============================

O(n log n). but bad O(n^2) if we select last element in almost sorted array as pivot

generally outperforms Merge Sort for sorting RAM-based arrays
*/

template<class T>
void exchg(T &a, T &b) {
	T tmp = b;
	b = a;
	a = tmp;
}

template<class  T>
int partition(T a[], int left, int right)
{
	T pivot = a[right];
	int i= left-1;
	int j=right;
	for(;;) {
		while(a[--j] > pivot);
		while(a[++i] < pivot);
		if(i>=j)
			break;
		exchg(a[i], a[j]);
	}
	exchg(a[right], a[i]);
	return i;
};

template<class T>
void quick(T a[], int left, int right) {
	if(left >= right)
		return;
	int p = partition(a, left, right);
	quick(a, left, p-1);
	quick(a, p+1, right);
}

void executeQuickSort() {
	char a[] = {'A','S','O','R','T','I','N','G','E','X','A','M','P','L','E'};
    quick(a, 0, sizeof(a)/sizeof(a[0])-1);
}

/*
 =============================
		Merge Sort
 =============================
O(n log n) but requires O(n) space.

merge sort is stable sort, parallelizes better, and more efficient at handling 
slow-to-access sequential media.

Often best choice for sorting linked list.

*/

void merge(int a[], const int low, const int mid, const int high) {
	int *temp = new int[high-low+1];

	int left = low;
	int right = mid+1;
	int curr = 0;
	// Merge 2 arrays into temp[]
	while(left<= mid && right <= high) {
		if (a[left] <= a[right]) {
			temp[curr] = a[left];
			left++;
		} else {
			temp[curr] = a[right];
			right++;
		}
		curr++;
	}

	if(left > mid) {
		for(int i=right; i<=high; i++) {
			temp[curr] = a[i];
			curr++;
		}
	} else {
		for(int i=left; i<=mid; i++) {
			temp[curr] = a[i];
			curr++;
		}
	}

	for(int i=0; i<=high-low; i++){
		a[i+low] = temp[i];
	}
	delete[] temp;
}

void merge_sort(int a[], const int low, const int high) {
	if (low >= high) return;
	int mid = (low + high) / 2;
	merge_sort(a, low, mid);
	merge_sort(a, mid+1, high);
	merge(a, low, mid, high);
}

void executeMergeSort() {
	int a[] = {38, 27, 43, 3, 9, 82, 10};
	int arraySize = sizeof(a)/sizeof(int);

	print(a, arraySize);

	merge_sort(a, 0, (arraySize-1) );   

	print(a, arraySize);
}

/*
 =============================
		Heap Sort
 =============================
Similar to Selection Sort. Find max element and put it at the end.

parent at index i; (where index starts at 1)
left child 2*i, right child 2*i+1

parent at index i; (where index starts at 0)
left child 2*i+1, right child 2*i+2


in-place algorithm. not stable sort. O(n log n)
*/

void heapify(int arr[], int n, int i){
	int root =i;
	int left = 2*i + 1;
	int right = 2*i+2;

	if (left < n && arr[left] > arr[root])
		root = left;

	if (right < n && arr[right] > arr[root])
		root = right;

	if (root != i) {
		swap(arr[i], arr[root]);
		heapify(arr, n, root);
	}
}

void heapsort(int arr[], int n) {
	// build heap
	for(int i=n/2-1; i>=0; i--) {
		heapify(arr, n, i);
	}

	for(int i=n-1; i>=0; i--) {
		// move root to the end
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}

void executeHeapSort() {
	int a[] = {19, 17, 16, 12, 9, 15, 1, 2, 11, 7, 3, 10, 14};
	int sz = sizeof(a)/sizeof(a[0]); 
	
	print(a, sz);
	cout << "----------------------------------" << endl;
	heapsort(a, sz);
	print(a, sz);
}



int main() {
	cout << "Bubble Sort" << endl;
	executeBubbleSort();
	cout << "\nInsertion Sort" << endl;
	executeInsertionSort();	
	cout << "\nShell Sort" << endl;
	executeShellSort();
	cout << "\nSelection Sort" << endl;
	executeSelectionSort();
	cout << "\nQuick Sort" << endl;
	executeQuickSort();
	cout << "\nMerge Sort" << endl;
	executeMergeSort();
	cout << "\nCounting Sort" << endl;
	executeCountingSort();
	cout << "\nRadix Sort" << endl;
	executeRadixSort();
	cout << "\nBucket Sort" << endl;
	executeBucketSort();
	cout << "\nHeap Sort" << endl;
	executeHeapSort();

	return 0;
}


