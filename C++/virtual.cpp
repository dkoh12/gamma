#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

// Polymorphism
// http://www.cplusplus.com/doc/tutorial/polymorphism/

using namespace std;

class Person {
protected:
	string name;
	int age;

public:
	virtual void getdata() =0;
	virtual void putdata() =0;
};

// int Professor::cur_id = 0;
// int Student::cur_id = 0;

static int prof_cur_id;
static int stu_cur_id;

class Professor : public Person {
private:
	int publications;
	// static int cur_id; // cannot initialize static member var inside class
	int id;

public:
	void getdata() {
		cin >> name >> age >> publications;
		prof_cur_id++;
		id = prof_cur_id;
	}

	void putdata() {
		cout << name << " " << age << " " << publications << " " << id << endl;
	}
};

class Student : public Person {
private:
	int marks[6];
	// static int cur_id;
	int id;

	int sum(int marks[], int size) {
		int total =0;
		for(int i=0; i< size; i++) {
			total += marks[i];
		}
		return total;
	}

public:
	void getdata() {
		cin >> name >> age;
		for(int i=0; i< 6; i++) {
			int x;
			cin >> x;
			marks[i] = x;
		}
		stu_cur_id++;
		id = stu_cur_id;
	}

	void putdata() {
		cout << name << " " << age << " " << sum(marks, 6) << " " << id << endl;
	}
};


// abstract base class
class Polygon {
protected:
	int width, height;
public:
	virtual ~Polygon(){}; // virtual destructor needed when @least one class method is virtual
	Polygon (int a, int b) : width(a), height(b) {}
	virtual int area () =0; // pure virtual func
	void printarea()
	{cout << this->area() << endl;}
};

class Rectangle: public Polygon {
public:
	~Rectangle(){};
	Rectangle(int a, int b) : Polygon(a, b) {}
	int area (void) {return (width * height);}
};

class Triangle: public Polygon {
public:
	~Triangle(){};
	Triangle(int a, int b) : Polygon(a, b) {}
	int area (void) {return (width * height/2);}
};


/*
need a virtual de
*/


/* (HackerRank)
Sample Input
4
1
Walter 56 99
2
Jesse 18 50 48 97 76 34 98
2
Pinkman 22 10 12 0 18 45 50
1
White 58 87

Sample Output
Walter 56 99 1
Jesse 18 403 1
Pinkman 22 135 2
White 58 87 2
*/
void executePerson() {
	int n, val;
	cin >> n;
	Person *per[n];

	for(int i=0;i<n;i++) {
		cin >> val;
		if(val == 1) {
			per[i] = new Professor;
		} else {
			per[i] = new Student;
		}

		per[i]->getdata();
	}

	for(int i=0; i<n;i++) {
		per[i]->putdata();
	}
}




int main()
{
	Polygon *poly1 = new Rectangle(4, 5);
	Polygon *poly2 = new Triangle(4,5);

	poly1->printarea();
	poly2->printarea();

	delete poly1;
	delete poly2;

	executePerson();


	return 0;
}








