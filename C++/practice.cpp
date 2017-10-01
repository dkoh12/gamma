#include <iostream>

using namespace std;



// object composition
// instance var that holds ptr to Animal object
// class Cat {
// private:
// 	Animal *animal;
// public:
// 	int makeSound() {
// 		return animal->cry();
// 	}
// };

// inheritance
//class Banimal {};
// class Bat : public Animal{
// public:
// 	void scream(){
// 		cout << "scream" << endl;
// 	}
// };



// class inheritance lets us define implementation of one class in terms of another class

//composition: new functionality is obtained by composing object. No internal details of objects are visible (black-box)
// contrary to class inheritance where internals 



class Animal {
public:
	virtual ~Animal() { 
		cout <<"deleted" << endl;
	};
	virtual void print() {
		cout << "hello" << endl;
	}
};

class Bat : public Animal {
public:
	~Bat() {
		cout << "bat deleted" <<endl;
	};
	void print() {
		cout << "world" << endl;
	}
};

int main() {
	Animal *a = new Bat();
	a->print();
	Animal *b = new Animal();
	b->print();

	// difference between -> and .
	Animal c;
	c.print();

	delete a;
	delete b;
	// delete &c;

	return 0;
}

