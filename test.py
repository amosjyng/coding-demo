f = open("demo.cpp", "a")
name = input("Enter your name: ")
f.write("""
#include <iostream>

int main() {{
    std::cout << "Hello {0}!";
    return 0;
}}
""".format(name))
f.close()
