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
    int b = 2;
    int *c = new int;
    cout << &b << endl;
    cout << &c << endl;
    cout << c << endl;
    c = reinterpret_cast<int*>(300);

    for (int i = 0; i < 500; i++) {
        cout << c[i] << endl;
    }
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;

    delete c;
    print_info("c", &c[2]);

    return 0; 
    // string a;
    // cin>>a;
}
