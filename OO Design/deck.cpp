#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


const string SUITE[4] = {"Hearts", "Diamonds", "Spades", "Clubs"};
const string RANK[13] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};


class Card {
private:
	string suite;
	string rank;
	friend class Deck;

public:
	// generate random card
	Card() {
		int suite = rand() % 4;
		int rank = rand() % 13;

		Card(SUITE[suite], RANK[rank]);
	}

	string getRank(){
		return rank;
	}

	string getSuite(){
		return suite;
	}

	Card(string s, string r) : suite(s), rank(r) {}

	void printCard() {
		cout << "card suite is " << suite << " and rank is " << rank << endl;
	}

	friend bool operator==(Card &left, Card &right) {
		if(left.suite == right.suite && left.rank == right.rank) {
			return true;
		}
		return false;
	}

	friend ostream& operator<<(ostream&, Card&);

};


class Deck {
private:
	vector<Card> deck;

public:
	// standard deck
	Deck() {
		for(int i=0; i<13; i++){
			for(int j=0; j<4; j++) {
				Card c(SUITE[j], RANK[i]);
				deck.push_back(c);
			}
		}
	}

	Deck(vector<Card> d) : deck(d) {}


	// error?
	// void printDeck(){
	// 	for(int i=0; deck.size(); i++){
	// 		cout << deck[i] << " ";
	// 	}
	// 	cout << endl;
	// }


	int size() {
		return deck.size();
	}

	void add(Card &c){
		deck.push_back(c);
	}

	void remove(){
		deck.erase(deck.begin());
	}

	Card draw() {
		Card c = deck[0];
		remove();
		return c;
	}

	void shuffle() {
		random_shuffle(deck.begin(), deck.end());
	}

	vector<vector<Card> > deal(int players, int handsize){
		vector<vector<Card> > hands;

		for(int i=0; i<handsize; i++) {
			for(int j=0; j<players; j++) {
				
				if(hands.size() < j+1) {
					vector<Card> hand;
					hands.push_back(hand);
				}

				Card c = draw();
				hands[j].push_back(c);
			}
		}

		return hands;
	}

	Card operator[](int i) const {
		return deck[i];
	}

};


ostream& operator<<(ostream& os, Card &c) {
	// c.getSuite()
	// c.getRank()
	os << c.suite << " " << c.rank << endl;
	return os;
}


int main() {

	// seed the psuedo-random number generator
	srand(time(0));

	Card d("heart", "5");
	// d.printCard();

	Card c("heart", "5");
	// c.printCard();

	// cout << (c == d) << endl;

	Deck deck;
	// deck.add(c);
	// deck.add(d);
	deck.shuffle();

	for(int i=0; i<deck.size(); i++) {
		Card c = deck[i];
		c.printCard();
	}

	vector<vector<Card> > hands = deck.deal(5, 5);

	for(int i=0; i<hands.size(); i++){
		cout << "new hand" << endl;
		for(int j=0; j<hands[i].size(); j++) {
			cout << hands[i][j];
		}
		cout << endl;
	}


	return 0;
}