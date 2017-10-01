
#include <iostream>
using namespace std;

#define NAME_SIZE 50

class Person {
	int id;
	char name[NAME_SIZE];

public:
	~Person() {
		cout << "deleteing a person." << endl;
	}

	void virtual aboutMe() {
		cout << "I am a person.\n";
	}

	virtual bool addCourse(string s) = 0;
};

class Student: public Person {
public:
	~Student() {
		cout << "deleteing a student." << endl;
	}

	void aboutMe() {
		cout << "I am a student.\n";
	}

	bool addCourse(string s) {
		cout << "Added course " << s << " to student." << endl;
		return true;
	}
};


void reverse(char *c) {
	char tmp;
	for (int i=0; i<strlen(c)/2; i++) {
		tmp = c[strlen(c)-1-i];
		c[strlen(c)-1-i] = c[i];
		c[i] = tmp;
	}

	cout << c << endl;
}

void flip(char* str) {
	reverse(str, str + strlen(str));

	cout << str << endl;
}

int main() {
	// Person *p = new Student();
	// p->aboutMe();
	// p->addCourse("History");
	// delete p;

	char s[] = "Hello";
	flip(s);

	char b[] = "GoodBye";
	reverse(b);

	return 0;
}

