#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

/**
 * 10 x 10 field. columns A-J, rows 1-10
 * 
 * Game has players
 * player has field
 * field has fleet
 * fleet has ships
 *
 * ships:
 * destroyer (2 squares)
 * submarine (3 squares)
 * cruiser (3 squares)
 * battleship (4 squares)
 * aircraft carrier (5 squares)
 */

map<string, int> getMap(){
	map<string, int> m;
	m["A"]=0;
	m["B"]=1;
	m["C"]=2;
	m["D"]=3;
	m["E"]=4;
	m["F"]=5;
	m["G"]=6;
	m["H"]=7;
	m["I"]=8;
	m["J"]=9;
	return m;
}


class Ship {
protected:
	bool sunk;
	string name;
	int numsquares;
public:
	Ship() = default;
	// ~Ship();

	string getName(){
		return name;
	}

	bool isSunk(){
		return sunk;
	}

};


class Destroyer : public Ship {
public:
	Destroyer(){
		name = "Destroyer";
		numsquares = 2;
	}
};

class Cruiser : public Ship {
public:
	Cruiser(){
		name = "Cruiser";
		numsquares = 3;
	}
};

class Submarine : public Ship {
public:
	Submarine(){
		name = "Submarine";
		numsquares = 3;
	}
};

class Battleship : public Ship {
public:
	Battleship(){
		name = "Battleship";
		numsquares = 4;
	}
};

class AircraftCarrier : public Ship {
public:
	AircraftCarrier() {
		name = "AircraftCarrier";
		numsquares = 5;
	}
};




class Fleet {
	vector<Ship> v;
public:
	void addShip(Ship b) {
		v.push_back(b);
	}
};

class Square {
	string location;
	Ship ship;
	int hit;
public:
	// c++11 feature
	// Square() = default;
	Square() {
		location = " ";
		hit=0;
	}

	Square(string loc, Ship s, int h) : location(loc), ship(s), hit(h) {}

	string getLocation(){
		return location;
	}

};

// https://isocpp.org/wiki/faq/operator-overloading#matrix-subscript-op
class Player {
private:
	// int row_, col_;
	Square *board;
	map<string, int> map = getMap();

	// Fleet fleet;
public:
	// ~Player();
	Player() {
		board = new Square[100]; //rows and cols are default 10 x 10
	}

	void displayBoard(){
		cout << "hi" << (board+1)->getLocation() << endl;

		cout << "  | ";
		for(int i=0; i<10; i++){
			cout << char('A' + i) << " | ";
		}
		cout << endl << string(43, '-') << endl;

		for(int i=0; i<10; i++){
			cout << i << " | ";
			for(int j=0; j<10; j++) {
				cout << (board + i + 10 * j)->getLocation() << " | ";
			}
			cout << endl << string(43, '-') << endl;
		}

	}

	bool enter(string shipname, string location) {

		cout << shipname << endl;
		cout << location << endl;

		string start = location.substr(0, location.find(","));
		string end = location.substr(location.find(",")+2);

		int x1 = map[start.substr(0,1)]; // this is a string
		int y1 = start[1] - '0';

		cout << "x1: " << x1 << endl;
		cout << "y1: " << y1 << endl;

		int x2 = map[end.substr(0,1)]; // this is a string
		int y2 = end[1] - '0';

		cout << "x2: " << x2 << endl;
		cout << "y2: " << y2 << endl;

		if (x1 != x2 && y1 != y2) {
			return false;
		}

		return true;
	}



	// Square operator()(int x, int y) {
	// 	if(x >= 10 or y >= 10){
	// 		printf("fail");
	// 		// throw BadIndex("error");
	// 	}

	// 	return board[y + x*10];
	// }

};


ostream& operator<<(ostream& os, Square& s){
	os << " testing: " << s.getLocation() << "\n";
	return os;
}


void playGame() {
	cout << "Hello and welcome to Battleship" << endl << endl;
	Player p;
	cout << "Here is your board. Please place your ships in 'start_position, end_position' ";
	cout << "such as A0, D0" << endl;
	p.displayBoard();

	cout << "Please enter 1 Battleship (4 squares)" << endl;
	string location = "A0, D0";
	
	while (!p.enter("battleship", location)){
		location = "A0, D0";
		cout << "invalid coordinates. please enter again" << endl;
	}

	p.displayBoard();


}


int main() {
	playGame();


	return 0;
}




