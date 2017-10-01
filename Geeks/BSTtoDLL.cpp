#include <iostream>

using namespace std;

struct Node {
	struct Node *left, *right;
	int data;
};


void BT2DLL(Node *root, Node **head) {
	if (root == nullptr) 
		return;

	static Node *prev = nullptr;
	BT2DLL(root->left, head);

	if(prev == nullptr)
		*head = root;
	else {
		root->left = prev;
		prev->right = root;
	}
	prev = root;

	BT2DLL(root->right, head);
}

Node* newNode(int data) {
	Node *new_Node = new Node;
	new_Node->left = new_Node->right = nullptr;
	new_Node->data = data;
	return new_Node;
}

void printlist(Node *node) {
	while (node!=nullptr) {
		cout << node->data <<" ";
		node = node->right;
	}
	cout << endl;
}

int main()
{
	Node *root 			= newNode(10);
	root->left 			= newNode(12);
	root->right 		= newNode(15);
	root->left->left 	= newNode(25);
	root->left->right 	= newNode(30);
	root->right->left 	= newNode(36);

	Node *head = nullptr;
	BT2DLL(root, &head);

	printlist(head);

	return 0;
}