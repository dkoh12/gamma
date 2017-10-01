import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

class Heap {
	private Queue<Integer> low = new PriorityQueue<>(Comparator.reverseOrder());
	private Queue<Integer> high = new PriorityQueue<>();

	public void add(int number) {
		Queue<Integer> target = low.size() <= high.size() ? low : high;
		target.add(number);
		balance();
	}

	private void balance() {
		while(!low.isEmpty() && !high.isEmpty() && low.peek() > high.peek()) {
			// poll is same as pop()
			Integer lowHead = low.poll();
			Integer highHead = high.poll();
			low.add(highHead);
			high.add(lowHead);
		}
	}

	public double median() {
		if(low.isEmpty() && high.isEmpty()) {
			throw new IllegalStateException("Heap is empty");
		} else {
			return low.size() == high.size() ? (low.peek() + high.peek())/2.0 : low.peek();
		}
	}

}


class RunningMedian {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] a = new int[n];

		Heap myHeap = new Heap();

		for(int i=0; i<n; i++){
			a[i] = in.nextInt();

			myHeap.add(a[i]);
			System.out.println(myHeap.median());
		}
	}
}