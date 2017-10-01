#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>

// http://www.bogotobogo.com/Algorithms/trie.php


/**
 * bottom-up
 * --------
 * start at smallest value. calculate any function using previously computed values at each step
 *
 * top-down
 * ---------
 * save each value that it computes as its final action. memoization.
 *
 */

using namespace std;

// #define max(a, b) ((a > b) ? a : b)

const int mmax = 100;


template< typename T, size_t N, size_t M>
void printMatrix(T(&arr)[N][M]) {
	for(int x=0; x<N; x++) {
		for(int y=0; y<M; y++) {
			cout << arr[x][y] << " ";
		}
		cout << endl;
	}
}

void printMatrix(vector<vector<int> > vec){
	cout << "vec.size " << vec.size() << endl;
	cout << "vec[i].size() " << vec[0].size() << endl;

	for(int i=0; i<vec.size(); i++) {
		for(int j=0; j<vec[i].size(); j++) {
			cout << vec[i][j] << " ";
		}
		cout << endl;
	}

	/*
	for(const auto &row : vec) {
		for(const auto &s : row) {
			cout << s << " ";
		}
		cout << endl;
	}*/
}

void print(int arr[], int n) {
	for(int i=0; i<n; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
} 

/*=============================================
=                 Knapsack                 =
=============================================*/
/**
 * O(2^n). For example K(1, 1) is being evaluated 2x
 */
//recursive way
int Knapsack(int W, int weight[], int value[], int n) {
	if (n==0 || W ==0)
		return 0;

	if (weight[n-1] > W)
		return Knapsack(W, weight, value, n-1);

	return max(Knapsack(W, weight, value, n-1), 
		value[n-1] + Knapsack(W-weight[n-1], weight, value, n-1));
}

/**
 * avoid recomputations using K[][]
 * O(nW) where n = # of items and W = capacity of knapsack
 *
 * s[] param is there to see the actual elements in your list.
 */
// DP way
int knapsack(int W, int weight[], int value[], int n, int s[]) {

	// 4 x 51 ??
	std::vector<std::vector<int> > m(n+1, std::vector<int>(W+1, 0)); // m[n+1][W+1]
	// int m[n+1][W+1];

	// build table in bottom up manner
	for(int j=0; j<=W; j++)
		m[0][j] = 0;

	for(int i=1; i<= n; i++) {
		for(int j=0; j<= W; j++) {
			//  don't understand this line
			if (weight[i-1] > j) {
				m[i][j] = m[i-1][j];
			}
			else {
				m[i][j] = max(m[i-1][j], value[i-1] + m[i-1][j-weight[i-1]]);
				s[j] = i;
			}
		}
	}
	
	// cout << "matrix" << endl;
	// printMatrix(m);

	return m[n][W];
}

int knapsackrepeat(int W, int weight[], int value[], int n) {
	int K[W+1];
	memset(K, 0, (W+1) * sizeof(int));

	for(int i=1; i<W+1; i++){
		for(int j=0; j<n; j++) {
			// don't understand the following line
			if (weight[j] < i)
				K[i] = max(K[i-weight[j]] + value[j], K[i]);
		}
	}

	// print(K, W);
	return K[W];
}

void executeKnapsack() {
	int weight[] = {10, 20, 30};
    int value[] = {60, 100, 120}; 
    int W = 50;
    int n = sizeof(value) / sizeof(value[0]);
    int *s = new int[W+1];

    cout << "max value: ";
    cout << knapsack(W, weight, value, n, s) << endl;  // $220
    cout << knapsackrepeat(W, weight, value, n) << endl;  // $220


    // see which weights were used
    int k= W;
    cout << "weights used: ";
    while(k) {
    	cout << weight[s[k]-1] << " ";
    	k -= weight[s[k]-1];
    }
    cout << endl;
}

/*=====  End of Section comment block  ======*/


/*===========================
=            Fibonacci       =
===========================*/
/*
recursive
 */

int fibo_rec(int n) {
	if(n==0) return 0;
	if(n==1) return 1;
	return fibo_rec(n-1) + fibo_rec(n-2);
}

/*
bottom up

fastest here.
 */
int fibo_bu(int n){
	int map[mmax];
	map[0] = 0;
	map[1] = 1;

	for(int i=2; i<=n; i++) 
		map[i] = map[i-1] + map[i-2];

	return map[n];
}

/*
top-down

slow for fibonacci
 */
int fibo_td(int n) {
	//initialized to 0
	static int map[mmax]; // I guess you can declare static var inside func
	if(map[n] > 0) return map[n];
	if(n==0 || n == 1)
		map[n] = n;
	else
		map[n] = fibo_td(n-1) + fibo_td(n-2);

	return map[n];
}

void executeFib(){
	cout << fibo_rec(10) << endl;
	cout << fibo_bu(10) << endl;
	cout << fibo_td(10) << endl;
}


/*=====  End of Fib  ======*/

/*============================================
=            ways to reach stairs            =
============================================*/
/*
can take 1, 2, 3 steps in any turn. find min turns to take n steps.
 */

int count(int n) {
	static int map[mmax];
	if(n<0) 
		return 0;
	if(n == 0) 
		return 1;
	if(map[n] > 0) 
		return map[n];

	map[n] = count(n-3) + count(n-2) + count(n-1);

	print(map, 12);

	return map[n];
}

void executeCount(){
	int steps = 10;
	cout << count(steps) << endl;
}

/*=====  End of ways to reach stairs  ======*/

/*===================================
=            Coin Change            =
===================================*/
/**
 * find min number of coins for change
 *
 * bottom-up
 */

int coinChangeRecurse(int amount, int d[], int n) {
	if (amount <= 0)
		return 0;

	int min_coins = INT_MAX; // 2147483647 == 2^31 - 1

	for(int i=0; i<n; i++) {
		if(d[i] <= amount) {
			min_coins = min(min_coins, coinChangeRecurse(amount-d[i], d, n) + 1);
		}
	}

	return min_coins;
}
/**
* int s[] is only necessary for denomination. 
* aka. see which coins not only the number of coins.
*
* O(nd) where n = amount and d = number of possible coins
*
* @C[] is an array where value @ each index == min # of coins for amount == index. 
 */
int coinChange(int amount, int coins[], int n, int C[], int s[]) {
	if (amount <= 0) {
		return 0;
	}

	C[0] = 0;

	for(int i=1; i <= amount; i++) {
		C[i] = INT_MAX;
		for(int j=0; j<n; j++) {
			/**
			 * i >= coins[j]
			 * -------------
			 * if index >= coin[j], that coin is available to use.
			 *
			 * 1 + C[i-coins[j]] < C[i]
			 * ------------------------
			 * if adding 1 coin to whatever we had previously makes less coins overall
			 * use that.
			 *
			 * for example if it took 1 coin to change $0.10. It would take 1+1 coins
			 * to change $0.15
			 *
			 * s[i] = j
			 * ---------
			 * record the largest last coin that you were able to use to return change.
			 *
			 * so for $0.06, j=0 (1)
			 * for $0.25 j=3 (25)
			 * for $0.55 j=1 (5)
			 */

			if (i >= coins[j] && 1 + C[i-coins[j]] < C[i]) {
				C[i] = 1 + C[i-coins[j]];
				// comment this out if you want.
				s[i] = j;
			}
		}
	}

	print(C, amount+1);
	print(s, amount+1);

	return C[amount];
}

void executeChange() {
	int coins[] = {1, 5, 10, 25};
    int amount = 67;
    int size = sizeof(coins)/sizeof(coins[0]);
    int *C = new int[amount+1]; // amount must be positive here
    int *s = new int[amount+1];
    int ans = coinChange(amount, coins, size, C, s);
    cout << "Minimal # of coins = " << ans << endl;

    cout << "coins used: ";
    int k = amount;
    while(k) {
    	cout << coins[s[k]] << " ";
    	k -= coins[s[k]];
    }
    cout << endl;
    delete[] C;
    delete[] s;
}

/*=====  End of Coin Change  ======*/

/*==================================================
=            Longest Common Subsequence            =
==================================================*/



int lcs(char *X, char *Y, int m, int n) {
	int L[m+1][n+1];
	int i,j;

	for(i=0;i<=m;i++) {
		for(j=0; j<=n; j++) {
			if (i==0 || j== 0)
				L[i][j] = 0;
			else if (X[i-1] == Y[j-1])
				L[i][j] = 1 + L[i-1][j-1];
			else
				L[i][j] = max(L[i-1][j], L[i][j-1]);
		}
	}

	return L[m][n];
}

void executeLCS() {
	char X[] = "AGGTAB";
	char Y[] = "GXTXAYB";
	int m = strlen(X);
	int n = strlen(Y);

	printf("%d\n", lcs(X, Y, m, n));

}


/*=====  End of Longest Common Subsequence  ======*/

/*======================================================
=            Longest Increasing Subsequence            =
======================================================*/


int lis(int arr[], int n) {
	int i, j;

	int *a = (int *) malloc(n*sizeof(int));

	// initialize all paths to 1
	for(i=0;i<n;i++){
		a[i] = 1;
	}

	for(i=1; i<n; i++) {
		for(j=0; j< i; j++) {
			if (arr[i] > arr[j] && a[i] < a[j]+1) {
				*(a+i) = *(a+j)+1;
			}
		}
	}

	// find max
	int mmax = 0;
	for(i=0; i<n;i++){
		if (mmax < a[i])
			mmax = a[i];
	}

	return mmax;

}


void executeLIS() {
	int arr[] = {10,22,9,33,21,50,41,60};
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("%d\n", lis(arr, n));

}

/*=====  End of Longest Increasing Subsequence  ======*/

/*=====================================
=            Edit Distance            =
=====================================*/

int editDistance(string s1, string s2, int m, int n) {

	int L[m+1][n+1];

	for(int i=0; i<=m; i++) {
		for(int j=0; j<=n; j++) {
			if (i==0)
				L[i][j] = j;
			else if (j==0)
				L[i][j] = i;

			else if (s1[i-1] == s2[j-1]) {
				L[i][j] = L[i-1][j-1];
			}
			else {
				L[i][j] = 1 + min(L[i][j-1], min(L[i-1][j], L[i-1][j-1]));
			}
		}
	}

	return L[m][n];

}


void executeEditDistance() {
	string s1 = "sunday";
	string s2 = "saturday";

	printf("%d\n", editDistance(s1, s2, s1.length(), s2.length()));
}

/*=====  End of Edit Distance  ======*/

/*=============================================
=            Minimum Sum Partition            =
=============================================*/
/**
 * find minimum value of difference of two sets
 *
 * O(n * sum) where n = # of elements, sum = sum of all elements
 */

int findMin(int arr[], int n) {
	int sum = 0;
	for(int i=0; i<n;i++)
		sum += arr[i];

	bool L[n+1][sum+1];

	for(int i=0;i<= n; i++)
		L[i][0] = true;

	for(int i=1; i<=sum; i++)
		L[0][i] = false;

	for(int i=1; i<=n; i++){
		for(int j=1; j<=sum; j++) {
			// if ith element is excluded
			L[i][j] = L[i-1][j];

			// if ith element is included
			if(arr[i-1] <= j)
				L[i][j] |= L[i-1][j-arr[i-1]];
		}
	}

	int diff = INT_MAX;

	// finds largest j where L[n][j] is true. 
	for(int j=sum/2; j>=0; j--) {
		if(L[n][j] == true) {
			diff = sum-2*j;
			break;
		}
	}

	return diff;
}


void executeMinDifference(){
	int arr[] = {3, 1, 4, 2, 2, 1};
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("%d\n", findMin(arr, n));
}


/*=====  End of Minimum Sum Partition  ======*/


/*=========================================
=            Stacking 3D Boxes            =
=========================================*/

/**
 * WE CAN USE MULTIPLE INSTANCE OF THE BOX!!!!!
 * 
 * Box can only be placed on top of another box only if both width 
 * and length of upper box is smaller than width and length of lower box.
 *
 * We can rotate these boxes.
 *
 * Variation of LIS problem.
 * 
 * 1. generate all 3 rotations of all boxes. size of rotation array becomes 3x 
 * size of original array
 *
 * 2. sort 3n boxes in decreasing order of base area
 *
 * 3. From there problem is same as LIS
 * MSH(i) = max possible stack height with box i at top.
 * MSH(i) = {Max (MSH(j)) + height(i)} where j < i and width(j) > width(i) 
 * and depth(j) > depth(i)
 * if there is no such j then MSH(i) = height(i)
 *
 * 4. To get overall height return max(MSH(i)) where 0 < i < n
 *
 *
 *
 * Time Complexity is O(n^2). 
 * Space: O(n)
 * 
 */

struct Box {
	int h, w, l;
};

int compare(const void *a, const void *b) {
	return ((*(Box *)b).l * (*(Box *)b).w ) - ((*(Box *)a).l * (*(Box *)a).w );
}

int maxStackHeight(Box arr[], int n) {
	Box rot[3*n];
	int index = 0;

	for (int i=0; i<n; i++) {
		// copy original box
		rot[index] = arr[i];
		index++;

		// first rotation
		rot[index].h = arr[i].w;
		rot[index].l = max(arr[i].h, arr[i].l);
		rot[index].w = min(arr[i].h, arr[i].l);
		index++;

		// second rotation
		rot[index].h = arr[i].l;
		rot[index].l = max(arr[i].h, arr[i].w);
		rot[index].w = min(arr[i].h, arr[i].w);
		index++;
	}

	// now number of boxes is 3n
	n = 3*n;

	qsort(rot, n, sizeof(rot[0]), compare);

	// initialize maximum stack height array
	int msh[n];
	for(int i=0; i<n; i++) {
		msh[i] = rot[i].h;
	}

	for(int i=1; i<n; i++) {
		for(int j=0; j<i; j++) {
			if(rot[i].w < rot[j].w &&
				rot[i].l < rot[j].l &&
				msh[i] < msh[j] + rot[i].h
				)
			{
				msh[i] = msh[j] + rot[i].h;
			}
		}
	}

	int mmax = INT_MIN;
	for(int i=0; i<n; i++) {
		if(mmax < msh[i]) {
			mmax = msh[i];
		}
	}

	return mmax;

}


void executeBox() {
	Box arr[] = {{4, 6, 7}, {1, 2, 3}, {4, 5, 6}, {10, 12, 32}};
	int n = sizeof(arr)/sizeof(arr[0]);

	cout << "max possible height of stack is " << maxStackHeight(arr, n) << endl;
}


/*=====  End of Stacking 3D Boxes  ======*/





int main() {
	cout << "Knapsack" << endl;
	executeKnapsack();
	cout << "\nFibonacci" << endl;
	executeFib();
	cout << "\nCount" << endl;
	executeCount();
	cout << "\nChange" << endl;
	executeChange();
	cout << "\nLCS" << endl;
	executeLCS();
	cout << "\nLIS" << endl;
	executeLIS();
	cout << "\nEdit Distance" << endl;
	executeEditDistance();
	cout << "\nMin Difference" << endl;
	executeMinDifference();

	cout << "\nMax Box Stack Height" << endl;
	executeBox();

	return 0;
}