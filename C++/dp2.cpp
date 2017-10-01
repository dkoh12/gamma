#include <iostream>
#include <vector>
#include <climits>

using namespace std;


// change 3 later if you change size
void print2D(int *M[3], int n) {

	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			cout << M[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}


/*==================================================
=            Optimal Binary Search Tree            =
==================================================*/

/*
http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/

each key has an associated frequency. searching a key at a lower level
will cost more frequency. find the minimum cost of a binary search tree.

 */

int sum(int freq[], int i, int j){
	int s =0;
	for(int k=i; k<=j; k++) {
		s += freq[k];
	}
	return s;
}

int optimalBST(int keys[], int freq[], int n) {

	int *cost[n];
	for(int i=0; i<n; i++){
		cost[i] = new int[n];
	}

	// fill in the diagonal first. 
	// same as if key[i] is a root
	for (int i=0; i<n; i++){
		cost[i][i] = freq[i];
	}

	// L = chain length
	for(int L=2; L<=n; L++) {
		// i = row
		for(int i=0; i<n-L+1; i++){
			//  j = col
			int j = i+L-1;

			cost[i][j] = INT_MAX;

			cout << "i " << i << " j " << j << endl;

			// try make all keys in interval [i..j] root
			for(int r=i; r<=j; r++) {
				int c = ((r > i) ? cost[i][r-1] : 0) +
						((r < j) ? cost[r+1][j] : 0) +
						sum(freq, i, j);

				if (c < cost[i][j])
					cost[i][j] = c;

			}
		}
	}



	print2D(cost, n);

	return cost[0][n-1];
}




void executeOptimalBST() {
	// keys should be sorted
	int keys[] = {10, 12, 20};
	int freq[] = {34, 8, 50};
	int n = sizeof(keys)/sizeof(keys[0]);

	cout << optimalBST(keys, freq, n) << endl;

}


/*=====  End of Optimal Binary Search Tree  ======*/





int main() {
	cout << "executeOptimalBST" << endl;
	executeOptimalBST();

	return 0;
}


