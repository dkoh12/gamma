#include <iostream>

using namespace std;

#define N 8


void printSolution(int board[N][N]){
	cout << endl;

	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			cout << board[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}


/**
 * Checks if queen can be placed.
 *
 * Since this function is only called when there are 'col' queens on board
 * we only need to check the left side for attacking queens.
 */
bool isSafe(int board[N][N], int row, int col) {
	int i, j;

	// check row on left side
	for(int i=0; i<col; i++)
		if (board[row][i])
			return false;

	// check upper diagonal on left side
	for(int i=row, j=col; i>=0 && j>=0; i--, j--) {
		if(board[i][j])
			return false;
	}

	// check lower diagonal on left side
	for(int i=row, j=col; i<N && j>=0; i++, j--) {
		if(board[i][j])
			return false;
	}

	return true;
}


bool solveNQueensUtil(int board[N][N], int col) {
	// if all queens are placed, return true
	if (col == N) {
		// uncomment this to see all possible solutions.
		// printSolution(board);
		return true;
	}

	for(int i=0; i<N; i++) {
		if(isSafe(board, i, col)) {
			// place queen
			board[i][col] = 1;

			// replace this w/ solveNQueensUtil(board, col+1) to get all possible boards
			// recurse to place rest of queens
			// solveNQueensUtil(board, col+1);
			if(solveNQueensUtil(board, col+1))
				return true;

			// backtrack. remove queen
			board[i][col] = 0;
		}
	}

	return false;

}



void solveNQueens(){
	int board[N][N] = {
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0},
		{0,0,0,0,0,0,0,0}
	};

	// delete bang
	if(!solveNQueensUtil(board, 0)) {
		cout << "Solution does not exist" << endl;
	}

	// comment this out
	printSolution(board);
}


int main() {

	solveNQueens();
	return 0;
}