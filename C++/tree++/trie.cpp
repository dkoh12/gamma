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
// http://www.bogotobogo.com/Algorithms/trie.php
// https://www.youtube.com/watch?v=AXjmTQ8LEoI

/**
 * L = avg Length of string
 * N = number of strings
 * 
 * Time is O(L + N)
 *
 *
 * prefix-based search : check if prefix exists or not
 * whole word search : check if whole word exists or not
 *
 *
 * deleting words in trie
 * abc
 * abgl
 * abcd
 *
 * if you want to delete abc but not abcd then mark d's flag as False.
 * 
 */


struct node {
	map<char, node*> children;
	bool end;

	node() {
		end = false;
	}
};

void insert(node* root, string s){
	for(int i=0; i<s.length(); i++){
		if(!root->children.count(s[i])) {
			root->children[s[i]] = new node;
		}
		root = root->children[s[i]];
	}
	root->end = true;
}

// search whole word
bool search(node* root, string s){
	for(int i=0; i<s.length(); i++) {
		if(!root->children.count(s[i]))
			return false;
		root = root->children[s[i]];
	}

	return root->end;
}

// searches just the prefix
bool searchPrefix(node* root, string s){
	for(int i=0; i<s.length(); i++){
		if (!root->children.count(s[i])){
			return false;
		}
		root = root->children[s[i]];
	}
	return true;
}

bool deleteWord(node* root, string s, int i){

	if (i == s.length()){
		// don't delete word since another word depends on it
		if(root->end && !root->children.empty()) {
			root->end = false;
			return false;
		}

		return true;
	}
	
	if(root->children.count(s[i])) {
		if (deleteWord(root->children[s[i]], s, i+1)) {
			root->children.erase(s[i]);
			return root->children.empty();
		}
	}

	return false;
}


void deleteWord(node* root, string s){
	deleteWord(root, s, 0);
}




/*
typedef struct node
{
	int mark;

	// works with unicode characters and such
	// map<Character, TreeNode> children;
	
	// just lowercase or just uppercase
	node* children[26];
} node;


node* get() {
	node* n = new node;
	n->mark = 0;
	for(int i=0; i<26; i++){
		n->children[i] = nullptr;
	}
	return n;
}

void insert(node* root, string s){
	for(int i=0; i<s.length(); i++) {
		int now = s[i] - 'a';
		if(root->children[now] == nullptr) {
			root->children[now] = get();
		}
		root = root->children[now];
		root->mark += 1;
	}
}
*/


int main() {

	node* root = new node;
	insert(root, "abc");
	insert(root, "abgl");
	insert(root, "cdf");
	insert(root, "abcd");
	insert(root, "lmn");

	assert (searchPrefix(root, "lo") == false);
	assert (searchPrefix(root, "ab") == true);

	assert (search(root, "abc") == true);
	assert (search(root, "ab") == false);
	assert (search(root, "lmn") == true);
	assert (search(root, "ghi") == false);

	deleteWord(root, "abc");
	assert(search(root, "abc") == false);
	deleteWord(root, "abgl");
	assert(search(root, "abcd") == true);
	assert(search(root, "abgl") == false);
	assert(searchPrefix(root, "abc") == true);


	return 0;
}


