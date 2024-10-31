#include <iostream>
#include "ue.h"
#include <fstream>
#include <string>

using namespace std;

#define PRINT_INFO(desc, x) std::cout << desc << ": " << x << std::endl;
#define PRINT(x) std::cout << x << std::endl;

int main(int argc,char *agrv []){
    if(argc == 1){
        PRINT("too few argument!");
    }
    else{
        PRINT("argument : ");
        PRINT(agrv[1]);
        if(string(agrv[1]) == "-h"){
            PRINT("reading ue header ......");
            ifstream infile(agrv[2]);
            if(!infile){
                cerr << "connot open file " << agrv[2] << endl;
                return -1;
            }

            UE ue;
            infile.read(ue.magic,20); // magic number of ue file

            infile.read(reinterpret_cast<char *>(&(ue.filesize)),4); // filesize of ue file

            infile.read(reinterpret_cast<char *>(&(ue.textsize)),4); // textsize of ue file

            infile.read(reinterpret_cast<char *>(&(ue.datasize)),4); // datasize of ue file

            infile.read(reinterpret_cast<char *>(&(ue.textptr)),8); // textptr

            infile.read(reinterpret_cast<char *>(&(ue.dataptr)),8); // dataptr

            PRINT_INFO("Magic Number", ue.magic);
            PRINT_INFO("File Size", ue.filesize);
            PRINT_INFO("Text Size", ue.textsize);
            PRINT_INFO("Data Size", ue.datasize);
            PRINT_INFO("Text Pointer", ue.textptr);
            PRINT_INFO("Data Pointer", ue.dataptr);
        }
    }
}