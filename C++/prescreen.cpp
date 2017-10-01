#include <iostream>

using namespace std;

/**
 * atoi() that can handle negative numbers
 */
int AtoI(char *str) {
	int res = 0;
	int sign = 1;
	int i=0;

	if(str[0] == '-'){
		sign = -1;
		i++;
	}

	for(; str[i] != '\0'; i++) {
		res = res*10 + str[i] - '0';
	}

	return sign*res;
}

void reverse(char str[], int length) {
	int start = 0;
	int end = length - 1;

	while(start < end) {
		swap(*(str+start), *(str+end));
		start++;
		end--;
	}
}


char *ItoA(int num, char* str, int base) {
	int i=0;
	bool isNegative = false;

	// handle 0 explicitly or else will return empty string
	if (num == 0) {
		str[i++] = '0';
		str[i] = '\0';
		return str;
	}

	//  negative numbers are handled only with base 10
	if (num < 0 && base == 10) {
		isNegative = true;
		num = -num;
	}

	while (num != 0) {
		int rem = num % base;
		str[i++] = (rem > 9) ? (rem - 10) + 'a' : rem + '0';
		num = num/base;
	}

	if (isNegative)
		str[i++] = '-';

	str[i] = '\0';

	reverse(str, i);

	return str;
}

void executeItoA() {
	cout << "itoa()" << endl;
	char str[100];
	cout << "Base:10 " << ItoA(1567, str, 10) << endl;
	cout << "Base:10 " << ItoA(-1567, str, 10) << endl;
    cout << "Base:2 " << ItoA(1567, str, 2) << endl;
    cout << "Base:8 " << ItoA(1567, str, 8) << endl;
    cout << "Base:16 " << ItoA(1567, str, 16) << endl;
}


void executeAtoI() {
	cout << "atoi()" << endl;
	char str[] = "89789";
	int val = AtoI(str);
	printf("%d\n", val);
}

int main() {
	executeAtoI();
	executeItoA();

	return 0;
}