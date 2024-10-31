#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <Python.h>
#include <assert.h>
#include <stdbool.h>

#ifdef __linux__
#include <unistd.h>
#endif

#define STATUS bool
#define OK true
#define FAILED false

#define byte unsigned char

#define FORI(LOOPNUM) for(int i=0;i<LOOPNUM;i++) // loop i

#define MIN(a, b) ((a) < (b) ? (a) : (b)) // min of a and b
#define MAX(a, b) ((a) > (b) ? (a) : (b)) // max of a and b

#define MALLOC(type, count) ((type*)malloc(sizeof(type) * (count)))
#define FREE(ptr) do { free(ptr); (ptr) = NULL; } while(0)

#define MAIN int main()

#define printint(data) printf("%d",data)
#define printchar(data) printf("%c",data)
#define printstr(data) printf("%s",data)

STATUS python(const char *code){
    if(code == NULL)return FAILED;

    Py_Initialize();

    PyRun_SimpleString(code);

    Py_Finalize();

    return OK;
}