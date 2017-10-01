import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/ctci-merge-sort/problem

class inversion {

	private static long countInversions(int[] arr) {
		int[] aux = arr.clone();
		return countInversions(arr, 0, arr.length - 1, aux);
	}

	private static long countInversions(int[] arr, int lo, int hi, int[] aux) {
		if (lo >= hi) 
			return 0;

		int mid = lo + (hi-lo)/2;

		long count = 0;
		count += countInversions(aux, lo, mid, arr);
		count += countInversions(aux, mid+1, hi, arr);
		count += merge(arr, lo, mid, hi, aux);

		return count;
	}

	private static long merge(int[] arr, int lo, int mid, int hi, int[] aux) {
		long count = 0;
		int i = lo, j=mid+1, k=lo;

		while (i <= mid || j<= hi) {
			if (i > mid) {
				arr[k++] = aux[j++];
			} else if (j > hi) {
				arr[k++] = aux[i++];
			} else if (aux[i] <= aux[j]) {
				arr[k++] = aux[i++];
			} else {
				arr[k++] = aux[j++];
				count += mid + 1 - i;
			}
		}

		return count;
	}


	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		int t = in.nextInt();
		for(int i=0; i<t; i++) {
			int n = in.nextInt();
			int arr[] = new int[n];
			for(int j=0; j<n; j++) {
				arr[j] = in.nextInt();
			}
			System.out.println(countInversions(arr));
		}
	}
}

