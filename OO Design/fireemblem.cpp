#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Unit {
private:
	string name;
	string type;

	int health;
	static int itemcap = 5;

	int movement;
	int luck;
	int speed;
	int res;
	int def;
	int skill;
	int strength;

	int level;
	int experience;

	bool rescued = false;
	bool active = false;
	bool alive = true;

	vector<Items> v;

	// item rank. A B C D E
	int hitpoints; 

	Items equipped;


	Items equip() {
		equipped = nullptr;

		for(int i=0; i<v.size(); i++){
			if (v[i].weapon()) {
				equipped = v[i];
			}
		}

		return equipped;
	}


public:

	int control; // 0 = blue unit, 1 = npc, 2 = red/enemy

	int getHealth() {
		return health;
	}

	virtual int attack() =0;

	virtual int rescue(Unit u) =0;

	virtual int move() =0;

	virtual int levelUp() =0;

	virtual void trade(Items i, Items j) =0;

	virtual void addItem(Items i) =0;

	virtual void deleteItem(Items i) =0;

	string getName() {
		return name;
	}

};


class Team {
	vector<Unit> team;
	int unitcap;
public:
	Team(int number, vector<Unit> t) {
		unitcap = number;
		team = t;
	}

	void addUnit(Unit u){
		team.push_back(u);
	}

	void removeUnit(Unit u){
		team.erase(find(team.begin(), team.end(), u));
	}


};


// have hashmap of effects for items
// such as rapier, brave sword, rune sword.

class Items {
private:
	string name;
	int totalUse;
	int amountLeft;
	int price;


	bool weapon;

	string rank;
	int attack;
	int hit;
	int crit;
	int avoid;
	int range;

	int effects;

public:
	int getCost(){
		return price;
	}

	int getTotalUse(){
		return totalUse;
	}

	int getAmountLeft(){
		return amountLeft;
	}

	string getName() {
		return name;
	}

};


class Terrain {
private:
	int bonus;
	bool walkable; // don't want it to go through walls
public:
	Terrain(int b, bool w) {
		bonus = b;
		walkable = w;
	}

	void addBonus(Unit u) =0;

	bool isWalkable(){
		return walkable;
	}
};

// fix !
class Square {
	pair<terrain, unit> p;

public:
	Square(Terrain ter, Unit u) {
		p.append(terr, u);
	}
};


// fix !
class Board {
	int width;
	int height;
	Square board[][];

public:
	Board(int w, int h) {
		width = w;
		height = h;
		board = new board[width][height];
	}
};

