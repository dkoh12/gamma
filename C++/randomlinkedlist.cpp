#include <iostream>
#include <vector>

using namespace std;

struct Node {
	int data;
	Node *next;
	Node *random;
};

// prepends to front
void prepend(struct Node *head, int n){
	Node *node = new Node;
	node->data = n;
	node->next = head;

	head = node;
}

// pops from front
int pop(struct Node *head) {
	Node *node = head;
	int ret = node->data;

	head = head->next;
	delete node;
	return ret;
}

void addNode(struct Node *head, int n) {
	Node *node = new Node;
	node->data = n;
	node->next = NULL;

	Node *curr = head;
	while (curr) {
		if (curr->next == NULL) {
			curr->next = node;
			return;
		}
		curr = curr->next;
	}
}

bool deleteNode(struct Node *head, Node *ptrDel) {
	Node *curr = head;

	if (ptrDel == head) {
		head = head->next;
		delete ptrDel;
		return true;
	}

	while(curr) {
		if(curr->next == ptrDel) {
			curr->next = ptrDel->next;
			delete ptrDel;
			return true;
		}
		curr = curr->next;
	}

	return false;
}

// http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/

// clone a linked list w/ next and random ptr
// https://www.youtube.com/watch?v=EHpS2TBfWQg
// 
// METHOD 1
// store mapping in hashtable
// time = O(n)
// space = O(n)

// curr->random = curr->random->random->next;
// curr = curr->next;


// METHOD 2
// or create copy between 2 nodes in the original linkedlist
// time = O(n)
// space = O(1)


struct Node clone(struct Node *head) {
	Node *curr = head;

	// insert copy nodes between all original nodes
	while(curr) {
		Node *copy = new Node;
		copy->data = curr->data;
		copy->next = curr->next;
		curr->next = copy;
		curr = curr->next->next;
	}

	curr = head;

	// assign random ptrs
	while(curr){
		curr->next->random = curr->random->next;
		curr = curr->net;
	}

	Node *orig = head;
	Node *copy = head->next;
	while (orig && copy) {
		orig->next = orig->next->next;
		copy->next = copy->next->next;
	}


	return copy;

}


int main() {

	Node *root = new Node;
	root->data = 'a';
	root->next = NULL;
	addNode(root, 'b');
	addNode(root, 'c');
	addNode(root, 'd');
	addNode(root, 'e');



	return 0;
}


