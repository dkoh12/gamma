// // http://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/

// using namespace std;
// #include <bits/stdc++.h>

// // max # of states in matching machines. = to sum of length of all keywords
// const int MAXS = 500;

// // # of char in alphabet
// const int MAXC = 26;

// int out[MAXS]; // output
// int f[MAXS]; //failures

// int g[MAXS][MAXC]; // goto function (trie)


// int buildMatchingMachine(string arr[], int k) {
// 	memset(out, 0, sizeof out);

// 	memset(g, -1, sizeof g);

// 	int states = 1;

// 	for(int i=0; i<k; i++) {
// 		const string &word = arr[i];
// 		int currentState = 0;

// 		for (int j=0; j<word.size(); j++) {
// 			int ch = word[j] - 'a';

// 			if (g[currentState][ch] == -1)
// 				g[currentState][ch] = states++;

// 			currentState = g[currentState][ch];
// 		}

// 		out[currentState] |= (1 << i);
// 	}

// 	for (int ch=0; ch<MAXC; ch++) {
// 		if (g[0][ch] == -1)
// 			g[0][ch] = 0;
// 	}

// 	memset(f, -1, sizeof f);

// 	queue<int> q;

// 	for(int ch=0; ch<MAXC; ch++) {
// 		if(g[0][ch] != 0) {
// 			f[g[0][ch]] = 0;
// 			q.push(g[0][ch]);
// 		}
// 	}

// 	while (q.size()) {
// 		int state = q.front();
// 		q.pop();

// 		for(int ch=0; ch<= MAXC; ch++) {
// 			if(g[state][ch] != -1) {
// 				int failure = f[state];

// 				while (g[failure][ch] == -1)
// 					failure = f[failure];

// 				failure = g[failure][ch];
// 					f[g[state][ch]] = failure;

// 				out[g[state][ch]] |= out[failure];

// 				q.push(g[state][ch]);
// 			}
// 		}
// 	}

// 	return states;
// }


// int findNextState(int currentState, char nextInput) {
// 	int answer = currentState;
// 	int ch = nextInput - 'a';

// 	while (g[answer][ch] == -1) 
// 		answer = f[answer];

// 	return g[answer][ch];
// }


// void searchWords(string arr[], int k, string text) {
// 	buildMatchingMachine(arr, k);

// 	int currentState = 0;

// 	for(int i=0; i<text.size(); i++) {
// 		currentState = findNextState(currentState, text[i]);

// 		if (out[currentState] == 0)
// 			continue;

// 		for(int j=0; j<k; j++) {
// 			if(out[currentState] & (1<<j)) {
// 				cout << "Word " << arr[j] << " appears from " << i-arr[j].size() + 1 << " to " << i << endl;
// 			}
// 		}
// 	}
// }


// int main() {
// 	string arr[] = {"he", "she", "hers", "his"};
// 	string text = "ahishers";
// 	int k = sizeof(arr)/sizeof(arr[0]);

// 	searchWords(arr, k, text);

// 	return 0;
// }


#include <iostream>
#include <string.h>

using namespace std;

int main(){
	char a[] = "ahishers";
	const char *s[] = {"he", "she", "hers", "his"};

	int strsize = strlen(a);
	int indexsize =  sizeof(s)/sizeof(s[0]);
	int prev = 0, cur = 0;

	for(int i = 0; i < strsize; i++){
		prev = i;

		for(int j = 0; j < indexsize; j++){
			while(a[prev] == s[j][cur] && cur != strlen(s[j]))
			{
				prev++;
				cur++;

				if(cur == strlen(s[j]))
					cout << "Word " << s[j] << " appears from " << i << " to " << i+cur-1 <<endl;
			}
			prev = i;
			cur = 0;
		}
	}
    return 0;
}




