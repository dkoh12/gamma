import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Graph {
	List<List<Integer>> adjLst;
	int size;

	public Graph(int size){
		this.size = size;
		while (size-- > 0) {
			adjLst.add(new ArrayList<Integer>());
		}
	}

	public void addEdge(int first, int second) {
		adjLst.get(first).add(second);
		adjLst.get(second).add(first);
	}	

	public int[] bfsShortestReach(int start) {
		int[] distances = new int[size];
		Array.fill(distances, -1);

		Queue<Integer> q = new LinkedList<>();

		que.add(start);
		distances[start] = 0
		HashSet<Integer> h = new HashSet<>();

		while (!q.isEmpty()) {
			Integer curr = q.pop();
			for(int node : adjLst.get(curr)) {
				if(!h.contains(node)) {
					q.add(node);
					h.add(node);
					distances[node] += distances[curr] + 6;
				}
			}
		}

		return distances;
	}
}


class Heap {
	private Queue<Integer> lo = new PriorityQueue<>(Comparator.reverseOrder());
	private Queue<Integer> hi = new PriorityQueue<>();

	public void add(int n) {
		Queue<Integer> m = low.size() < hi.size() ? lo : hi;
		m.add(n);
		balance();
	}

	private void balance() {
		while(!lo.isEmpty() && !hi.isEmpty() && lo.peek() > hi.peek()) {
			Integer lowHead = lo.poll();
			Integer hiHead = hi.poll();
			lo.add(hiHead);
			hi.add(lowHead);
		}
	}

	public double median() {
		if (low.isEmpty() and hi.isEmpty()) {
			throw new IllegalStateException("Heap is empty");
		} else {
			return low.size() == hi.size() ? (low.peek() + hi.peek()) / 2 : low.peek();
		}
	}

}


class Node {
	Node[] children;
	boolean end;

	Node() {
		this.children = new Node[26];
		this.end = false;
	}

	public void insert(Node curr, String word) {
		for(char c : word.toCharArray()) {
			int index = c - 'a';

			if (curr.children[index] == null) {
				curr.children[index] = new Node();
			}

			curr = curr.children[index];
		}
		curr.end = true;
	}
}



class test {

	public static void main(String[] args) {

		// hashtable
		System.out.println("hashtable");

		Hashtable<String, Integer> h = new Hashtable<String, Integer>();

		h.put("Alfred", new Integer(1));
		h.put("Bob", new Integer(2));
		h.put("Carl", new Integer(3));
		h.put("Dave", new Integer(4));

		System.out.println(h.size());
		h.remove("Dave");

		System.out.println(h.isEmpty());
		System.out.println(h.size());
		h.replace("Carl", new Integer(5));

		System.out.println(h.toString());

		// System.out.println(h.elements().toString());


		// list
		List<String> myList = new ArrayList<>();

		myList.add("Hello");
		myList.add("World");
		myList.add("!!!");

		System.out.println(myList.toString());
		Collections.shuffle(myList);
		System.out.println(myList.toString());



		String[] suit = new String[] {
			"spades", "hearts", "diamonds", "clubs"
		};

		String[] rank = new String[] {
			"ace", "2", "3", "4", "5", "6", "7",
			"8", "9", "10", "jack", "queen", "king"
		};

		List<String> deck = new ArrayList<String>();
		for(int i=0; i<suit.length; i++){
			for(int j=0; j<rank.length; j++) {
				deck.add(rank[j] + " of " + suit[i]);
			}
		}

		Collections.shuffle(deck);
		List<String> hand = deck.subList(0, 5);
		System.out.println(hand.toString());

		// Stack
		
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(17);
		int a = stack.pop();
		System.out.println(a);

		// queue

		Queue<String> queue = new PriorityQueue<>();
		queue.add("hi");
		queue.add("bye");

		System.out.println(queue.toString());

		Queue<Integer> q = new LinkedList<>();
		Hashset<Integer> hh = new Hashset<>();


		Scanner in = new Scanner(System.in);
		int n = in.nextInt();

		while (n-- > 0) {
			int m = in.nextInt();
		}


	}

}


