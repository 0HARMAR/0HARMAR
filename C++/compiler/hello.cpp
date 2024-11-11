#include <iostream>
#include <string>
using namespace std;

template <typename StreamType>
StreamType
open(string filename){
    StreamType file(filename);
    if(!file.isopen()){
        cerr << "connot open file tokens.json" << endl;
        return nullptr;
    }
    else{
        return file;
    }
}

int main(){
    std::cout << "hello";
    int a = 1;
}