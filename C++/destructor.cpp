#include <vector>
#include <string>

class ShoppingCart
{
private:
	std::vector<std::string>* items;
public:
	ShoppingCart() {
		items = new std::vector<std::string>();
	}

	~ShoppingCart() {
		printf("deleted!\n");
		delete items;
	}

	void addItem(std::string item) {
		items->push_back(item);
	}

};


int main() {

	ShoppingCart art; // allocated on stack. destructor called automatically once out of scope
	art.addItem("eggs");
	art.addItem("cheese");


	ShoppingCart* cart = new ShoppingCart(); // dynamically allocated
	cart->addItem("milk");
	cart->addItem("bread");
	delete cart; // calls ~ShoppingCart for cart 

	return 0;
}

// when art goes out of scope
// ~ShoppingCart is automatically called
