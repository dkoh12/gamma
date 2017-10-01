#include <stdio.h>
#include <stdlib.h>

// calculate height in same recursion rather than calling height() separately
// O(n)

struct node {
	int data;
	struct node* left;
	struct node* right;
};

int isBalanced(struct node *root, int* height)
{
	// height of left & right subtrees
	int lh =0, rh =0;

	// l will be true if left subtree balanced
	// ditto right
	int l=0, r=0;

	if (root == NULL)
	{
		*height = 0;
		return 1;
	}

	l = isBalanced(root->left, &lh);
	r = isBalanced(root->right, &rh);

	*height = (lh > rh ? lh : rh) + 1;

	// tree is not balanced
	if((lh - rh >= 2) || (rh-lh >= 2))
		return 0;

	return 1;

}





// test

struct node* newNode(int data)
{
	struct node* node = (struct node*) malloc (sizeof(struct node));

	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return (node);
}

int main()
{
	int height =0;

	struct node *root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->left->left->left = newNode(7);

	if(isBalanced(root, &height))
		printf("tree is balanced");
	else
		printf("tree is not balanced");

	getchar();
	return 0;
}