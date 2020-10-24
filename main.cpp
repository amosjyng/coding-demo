#include <iostream>

using namespace std;

void print_info(string name, int *number) {
    cout << name << " is located at memory address " << number 
         << " and has value " << *number << endl;
}

int main() 
{
    int a = 10;
    int f[]={1,2,3,4};
    int b[500];
    for (int i = 0; i < 500; i++) {
        b[i] = i;
    }
    int *c;
    c = new int;
    *c = 30;
    print_info("a", &a);
    print_info("b", &b[2]);
    print_info("c", c);
    return 0; 
}
