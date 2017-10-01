#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/**
 *https://www.careercup.com/question?id=5638730112040960
 *
 * Design OO food delivery app catering to use cases - 
 * 
1) User can search different restaurant 
2) User can select a restaurant 
3) User sees a menu 
4) Restaurant can change the menu any time 
5) User adds an item from menu 
6) User orders the food 
7) User can track the order in real time 
8) User can cancel the order 
9) User pays for the order
 *
 */


/**
Design Patterns:

1. Builder Design Pattern (adding food item and ordering)
2. Interpreter Design Pattern (users can search different restaurants)
3. Iterator Pattern (user sees menu)
4. observer pattern (track an order in real time)
5. command pattern (order or cancellation of food)

 */


// How exactly does the user interact with the system?
// 

class Users {
private:
	string name;
public:
	Users(_name) : name(_name) {}

	string search(string restaurant) {
		return restaurant;
	}

	void newOrder(){

	}

	void trackOrder() {

	}

	void cancelOrder() {

	}

	void payBill() {

	}

};

// Composition
// 
// Restaurant HAS-A menu
// 
class Restaurant {
private:
	Menu menu;
	vector<Order> orders;
	bool open = false;
	string location;

public:

	void addToMenu(Food item){
		menu.add(item);
	}

	void deleteFromMenu(Food item){
		menu.delete(item);
	}

	void displayMenu(){
		menu.show();
	}

	void newOrder(Order order) {
		orders.push_back(order);
	}

	void getLocation(){
		return location;
	}

	bool isOpen(){
		return open;
	}
};


class Menu {
private:
	vector<Food> menu;
public:
	Menu() {}
	Menu(vector<Food> m) : menu(m) {}

	void add(Food item) {
		menu.push_back(item);
	}

	void delete(Food item) {
		// could error
		menu.erase(menu.begin(), menu.end(), item);
	}

	void show() {
		for(int i=0; i<menu.size(); i++){
			cout << menu[i] << endl;
		}
	}


	/*----------  Operator Overloads  ----------*/
	

	// not sure if const is necessary
	Food operator[](int i) const {
		return menu[i];
	}

	ostream& operator<<(ostream& os, Food& item) {
		os << item << '\n';
		return os;
	}
};


class Food {
private:
	string name;
	int rating;
	int price;

public:
	Food(_name, _price) : name(_name), price(_price) {}

	void setPrice(int i){
		price = i;
	}

	int getPrice(){
		return price;
	}

	void rate(int i){
		if ( 0 <= i <= 10)
			rating = i;
	}

	int getRating(){
		return rating;
	}

};

class Order {
private:
	int id;
	vector<Food> myOrder;
	int totalCost;
	bool delivery = false;
	string status;

	int getTotalCost(){
		return totalCost;
	}

public:
	Order() : id(rand()) {}

	string trackStatus() {
		return status
	}

	void remove(Food item){
		Food f = find(myOrder.begin(), myOrder.end(), item);
		totalCost -= f.getPrice();
		myOrder.erase(f);
	}

	void order(Food item){
		myOrder.push_back(item);
		totalCost += item.getPrice();
	}

	void cancel(){
		if (!delivery) {
			order.clear();
			totalCost = 0;
		}
	}

	void delivering(){
		delivery = !delivery;
	}
};


// Not sure if Bill should be a subclass of Order?
// Or an interface?

class Bill : public Order {
private:
	int billId;
	bool paid = false;

public:
	Bill() : billId(rand()) {}

	void displayBill() {
		cout << getTotalCost() << endl;
	}

	void pay(string payment_type){
		paid = !paid;
	}

	bool didpay(){
		return paid;
	}
};



int main() {
	srand(time(0));

	User u("john");
	User jack("jack");

	Menu m;
	Food hamburger("hamburger", "5");
	Food hotdog("hotdog", "3");
	Food frenchfry("frenchfry", "2");
	m.add(hamburger);
	m.add(hotdog);
	m.add(frenchfry);
	m.show();

	Order o;
	o.order(m[2]);

	Order oo;
	oo.order(m[1]);

	Bill b;



	return 0;
}




