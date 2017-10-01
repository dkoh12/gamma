import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

class Graph {
	List<List<Integer>> adjLst;
	int size;

	public Graph(int size) {
		adjLst = new ArrayList<>();
		this.size = size;
		while(size-- > 0) {
			adjLst.add(new ArrayList<Integer>());
		}
	}


	public void addEdge(int first, int second) {
		adjLst.get(first).add(second);
		adjLst.get(second).add(first);
	}

	public int[] bfsShortestReach(int startId) {
		int[] distances = new int[size];
		Arrays.fill(distances, -1);
		Queue<Integer> que = new LinkedList<>();

		que.add(startId);
		distances[startId] = 0;
		HashSet<Integer> seen = new HashSet<>();

		seen.add(startId);
		while(!que.isEmpty()) {
			Integer curr = que.poll();
			for(int node : adjLst.get(curr)) {
				if(!seen.contains(node)) {
					// offer is same as add but doesn't throw exception
					que.offer(node);
					seen.add(node);
					distances[node] = distances[curr] + 6;
				}
			}
		}

		return distances;
	}

}

class shortestReach {


	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();

		while(n-- > 0) {
			int N = in.nextInt();
			int m = in.nextInt();

			Graph graph = new Graph(N+1);

			while(m-- > 0) {
				int u = in.nextInt();
				int v = in.nextInt();
				graph.addEdge(u, v);
			}

			int start = in.nextInt();
			int[] distances = graph.bfsShortestReach(start);
		
			for(int i=1; i<distances.length; i++) {
				if (i != start)
					System.out.print(distances[i] + " ");
			}

			System.out.println();
		}
	}
}
