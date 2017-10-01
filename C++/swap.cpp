#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

// g++ swap.cpp -o swap

using namespace std;

void printarray(vector<int> arr);

void reverse(vector<int> arr, int n) {
    int temp, i;
    for (i=0; i!=arr.size()/2; i++) {
        temp = arr[n-i-1];
        arr[n-i-1] = arr[i];
        arr[i] = temp;
    }
    
    printarray(arr);
}

template <typename T>
void swap2(T& x, T& y) { // swap() conflicts with std::swap()
	T tmp = x;
	x = y;
	y = tmp;
};


void swapstar(int *a, int *b) {
	// int temp = *a;
	// *a = *b;
	// *b = temp;

	*a = *a ^ *b;
	*b = *a ^ *b;
	*a = *a ^ *b;
}


void swapxor(int &x, int&y) {
	x = x ^ y;
	y = x ^ y;
	x = x ^ y;
}



//void reverseArray(vec)

void printarray(vector<int> arr) {
    for(int i=0; i< arr.size(); ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){
    // int n;
    // cin >> n;
    // vector<int> arr(n);
    // for(int arr_i = 0;arr_i < n;arr_i++){
    //    cin >> arr[arr_i];
    // }
    
    //printarray(arr);
    // reverse(arr, n);
    
    //reverse(arr.begin(), arr.end());
    
    int a = 1, b=2;
    swap2(a, b);
    cout << "a: " << a << " b: " << b << endl;

    string c = "one", d = "two";
    swap2(c, d);
    cout << "c: " << c << " d: " << d << endl;

    int x=5, y=8;
    swapxor(x, y);
    cout << "x: " << x << " y: " << y <<endl;

    swapstar(&x, &y);
    cout << "x: " << x << " y: " << y <<endl;

    return 0;
}



