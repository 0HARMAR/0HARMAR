#include <iostream>
#include <fstream>
#include <cstring>
#include <cerrno>
#include "judge_linux.c"

using namespace std;

#define PRINT(x) std::cout << x << std::endl;

int main() {
    ofstream outFile;

    if(_system == _LINUX)
    outFile.open("/mnt/Just-For-Fun/C++/unixexecutable/mini.ue", ios::binary);
    else
    outFile.open("/mnt/c/Just-For-Fun/C++/unixexecutable/mini.ue", ios::binary);

    if (!outFile) {
        cerr << "Error opening file" << " " << strerror(errno) << endl;    
        return -1;
    }

    char buffer[20];
    memset(buffer, ' ', sizeof(buffer));
    memcpy(buffer, "ue format file", 14);

    outFile.write(buffer, sizeof(buffer)); // file magic

    int filesize = 42;
    outFile.write(reinterpret_cast<const char*>(&filesize), sizeof(filesize)); // file size

    int textsize = 42;
    outFile.write(reinterpret_cast<const char*>(&textsize), sizeof(textsize)); // text size

    int datasize = 0;
    outFile.write(reinterpret_cast<const char*>(&datasize), sizeof(datasize)); // data size

    void* textptr = nullptr;
    void* dataptr = nullptr;
    outFile.write(reinterpret_cast<const char*>(&textptr), sizeof(textptr));
    outFile.write(reinterpret_cast<const char*>(&dataptr), sizeof(dataptr));

    unsigned char code[] = {
        0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00, // mov $0x1, %rax
        0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00, // mov $0x1, %rdi
        0x48, 0x8d, 0x35, 0x15, 0x00, 0x00, 0x00, // lea (0x15)(%rip), %rsi
        0x48, 0xc7, 0xc2, 0x1c, 0x00, 0x00, 0x00, // mov $0x1c, %rdx
        0x0f, 0x05,                             // syscall
        0x48, 0xc7, 0xc0, 0x3c, 0x00, 0x00, 0x00, // mov $0x3c, %rax
        0x48, 0x31, 0xff,                       // xor %rdi, %rdi
        0x0f, 0x05                              // syscall
    };

    outFile.write(reinterpret_cast<const char *>(code),sizeof(code));

    unsigned char data[] = {
    0x1b, 0x5b, 0x30, 
    0x31, 0x3b,       
    0x33, 0x31,       
    0x6d,             
    0x48,             
    0x65, 0x6c,       
    0x6c,             
    0x6f,             
    0x2c, 0x20,       
    0x4f, 0x53,       
    0x20, 0x57, 0x6f, 
    0x72, 0x6c,       
    0x64, 0x1b, 0x5b, 0x30,
    0x6d,             
    0x0a              
    };

    outFile.write(reinterpret_cast<const char *>(data),sizeof(data));

    if (!outFile) {
        cerr << "Error writing to file" << endl;
        return -1;
    }

    PRINT("Write over!");

    outFile.close();
    return 0;
}
