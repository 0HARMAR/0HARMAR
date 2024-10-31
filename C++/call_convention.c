int add(int a,int b){
    int c = a * b + a - b;
    return c;
}

int main(){
    volatile int d = add(2,3);
}