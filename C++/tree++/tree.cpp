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
 * Least Common Ancestor in a binary tree
 * 
 * time: O(n)
 * space: O(n)
 */


struct node {
	node* left;
	node* right;
	int data;
};

node* newNode(int k) {
	node* n = new node;
	n->data = k;
	n->left = nullptr;
	n->right = nullptr;
	return n;
}

node* least_common_ancestor(node *root, int first, int second){
	if(root == nullptr)
		return nullptr;

	if (root->data == first || root->data == second)
		return root;

	node* left = least_common_ancestor(root->left, first, second);
	node* right = least_common_ancestor(root->right, first, second);

	// this is the LCA
	if (left && right){
		return root;
	}

	// check subtrees
	return left != nullptr ? left : right;
}


node* bst_least_common_ancestor(node* root, int first, int second){
	if (root == nullptr)
		return nullptr;

	if (root->data < first && root->data < second) {
		return bst_least_common_ancestor(root->right, first, second);
	}

	if (root->data > first && root->data > second) {
		return bst_least_common_ancestor(root->left, first, second);
	}

	return root;
}

// http://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
// https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better/2
// O(n)
int dfsHeight(node *root) {
	if (root == NULL)
		return 0;

	int leftHeight = dfsHeight(root->left);
	if (leftHeight == -1)
		return -1

	int rightHeight = dfsHeight(root->right);
	if (rightHeight == -1)
		return -1

	if (abs(leftHeight - rightHeight) > 1)
		return -1

	return max(leftHeight, rightHeight) + 1;
}

// is the binary tree balanced?
bool isBalanced(node *root) {
	return dfsHeight(root) != -1;
}



void binarytree() {
	node* root = newNode(3);
	root->left = newNode(6);
	root->left->left = newNode(2);
	root->left->right = newNode(11);
	root->left->right->left = newNode(9);
	root->left->right->right = newNode(5);
	root->right = newNode(8);
	root->right->right = newNode(13);
	root->right->right->left = newNode(7);

	cout << least_common_ancestor(root, 2, 5)->data << endl;
}

void binarysearchtree() {
	node* root = newNode(20);
	root->right = newNode(22);
	root->left = newNode(8);
	root->left->left = newNode(4);
	root->left->right = newNode(12);
	root->left->right->left = newNode(10);
	root->left->right->right = newNode(14);

	cout << least_common_ancestor(root, 22, 14)->data << endl;
	cout << least_common_ancestor(root, 4, 14)->data << endl;
	cout << least_common_ancestor(root, 10, 12)->data << endl;
}

// https://www.youtube.com/watch?v=13m9ZCB8gjw
int main() {
	binarytree();
	binarysearchtree();

	return 0;
}