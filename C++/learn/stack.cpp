#include <iostream>
using namespace std;

template <typename T>
class Stack {
private:
    T* arr;
    int top;
    int capacity;

public:
    Stack(int size) : top(-1), capacity(size) {
        arr = new T[capacity];
    }

    ~Stack() {
        delete[] arr;
    }

    void push(T x) {
        if (top == capacity - 1) {
            cout << "Stack overflow" << endl;
            return;
        }
        arr[++top] = x;
    }

    T pop() {
        if (top == -1) {
            cout << "Stack underflow" << endl;
            return T(); // 返回默认值
        }
        return arr[top--];
    }

    bool isEmpty() {
        return top == -1;
    }

    T peek() {
        if (!isEmpty()) return arr[top];
        throw out_of_range("Stack is empty");
    }
};

int main() {
    Stack<int> stack(5);
    stack.push(1);
    stack.push(2);
    cout << "Top element: " << stack.peek() << endl;
    cout << "Popped element: " << stack.pop() << endl;
    return 0;
}
