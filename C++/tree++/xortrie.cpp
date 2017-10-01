#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <string>
#include <stack>
#include <assert.h>

using namespace std;

/**
 *
 * Space taken by trie is O(n log n)
 * Insert & Query takes O(log n)
 * 
 */



struct node {
	node* children[2];
	bool end;
};

node* newNode(){
	node *n = new node;
	n->end = false;
	n->children[0] = nullptr;
	n->children[1] = nullptr;
	return n;
}

bool check(int x, int i){
	return (bool) (x & (1 << i));
}

void insert(node *root, int x){
	// pad up to 32 bits
	for(int i=31; i>=0; i--) {
		int f = check(x, i);
		if(!root->children[f]) {
			root->children[f] = newNode();
		}
		root = root->children[f];
	}
	root->end = true;
}

int query(node* root, int x){
	int ans = 0;
	for(int i=31;i>=0; i--){
		int f = check(x, i);

		cout << "i: " << i << " f: " << f << endl;

		// move to child whose xor with f is 1
		if(root->children[f ^ 1]) {
			ans += 1 << i;
			root = root->children[f ^ 1];
		}
		// if child with xor 1 doesn't exist
		else {
			root = root->children[f];
		}
	}

	return ans;
}

int main() {
	node *root = newNode();
	insert(root, 10);
	insert(root, 13);

	cout << query(root, 10) << endl;

	insert(root, 9);
	insert(root, 5);

	// cout << query(root, 6) << endl;

	return 0;
}