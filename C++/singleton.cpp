#include <iostream>

using namespace std;

/*
Purpose of Singleton?

http://www.bogotobogo.com/DesignPatterns/singleton.php


*/

class Singleton {
public:
	static Singleton *getInstance();

private:
	Singleton(){}
	static Singleton* instance;
};

Singleton* Singleton::instance = 0;
Singleton* Singleton::getInstance()
{
	if(!instance){
		instance = new Singleton();
		cout << "getInstance(): First instance" << endl;
		return instance;
	} else {
		cout << "getInstance(): Second instance" << endl;
		return instance;
	}


}

int main()
{
	Singleton *s1 = Singleton::getInstance();
	Singleton *s2 = Singleton::getInstance();
	return 0;
}