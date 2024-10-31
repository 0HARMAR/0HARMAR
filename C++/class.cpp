#include <iostream>

class Person {
public:
    std::string name;

private:
    int age;

public:
    void introduce() {
        std::cout << "My name is " << name << " and I am " << age << " years old." << std::endl;
    }

    void setage(int agrv)
    {
        age=agrv;
    }

    void printage()
    {
        std::cout << "age is " << age << std::endl; 
    }
};

int main() {
    Person person;
    person.name = "Alice";
    person.setage(30);
    person.printage();
    person.introduce();
    return 0;
}

