// http://www.artima.com/designtechniques/compoinh3.html

#include <iostream>

using namespace std;


/**
 * Inheritance 
 */

class Fruity {
public:
	int peel(){
		cout << "peel" << endl;
		return 1;
	}
};

class Banana : public Fruity {

};



/**
 * Composition
 */

class Fruit {
public:
	int peel(){
		cout << "peel" << endl;
		return 1;
	}
};

class Apple {
private:
	Fruit fruit;
public:
	int peel() {
		return fruit.peel();
	}
};


int main() {
	Banana b;
	int p = b.peel();
	cout << p << endl;

	Apple a;
	int pieces = a.peel();
	cout << pieces << endl;

	return 0;
}
