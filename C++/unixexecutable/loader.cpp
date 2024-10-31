#include <iostream>
#include "ue.h"
#include <fstream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

#define PRINT_INFO(desc, x) std::cout << desc << ": " << x << std::endl;
#define PRINT(x) std::cout << x << std::endl;

int main(int agrc,char *agrv[]){
    if(agrc == 1){
        PRINT("too few argument!");
    }
    else{
        ifstream infile(agrv[1],std::ios::binary);
        if(!infile){
                cerr << "connot open file " << agrv[2] << endl;
                return -1;
            }
        int textsize;

        infile.read(reinterpret_cast<char *>(&textsize),4);

        char text[42];

        infile.seekg(UEHEADER);

        infile.read(reinterpret_cast<char *>(text),textsize);

        PRINT(text);
    }
}