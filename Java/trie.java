import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/ctci-contacts/problem

class Node {
	int count;
	Node[] children;

	Node() {
		this.count = 0;
		this.children = new Node[26];
		Arrays.fill(children, null);
	}

	public void insert(Node curr, String value) {
		for( char c : value.toCharArray()) {
			int index = c - 'a';

			if (curr.children[index] == null) {
				curr.children[index] = new Node();
			}

			curr.children[index].count++;
			curr = curr.children[index];
		}
	}
}

class trie {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		Node trie = new Node();
		int n = scan.nextInt();

		while(n-- > 0) {
			String operation = scan.next();
			String value = scan.next();

			if(operation.equals("add")) {
				trie.insert(trie, value);
			}
			else {
				Node curr = trie;

				for(char c : value.toCharArray()) {
					curr = curr.children[c-'a'];

					if (curr == null)
						break;
				}

				System.out.println((curr != null) ? curr.count : 0);
			}
		}

		scan.close();
	}
}

