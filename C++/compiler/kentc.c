#include <stdlib.h>
#include <stdio.h>
#include <direct.h>

int main(){
    //change the current powershell session coding
    const char *setEncodingCommand = "powershell -ExecutionPolicy Bypass -File " 
    "C:\\Just-For-Fun\\C++\\compiler\\set_encoding.ps1";
    system(setEncodingCommand);
    //first step 
    //execute lexer,generate tokens.json
    const char *command1 = "python C:\\Just-For-Fun\\C++\\compiler\\lexer.py";
    int result = system(command1);
    if (result == 0){
        printf("执行成功");
    }
    else{
        perror("执行失败");
    }

    const char * go_path = "C:\\Just-For-Fun\\C++\\compiler\\go_used";
    if (_chdir(go_path) == 0){
        printf("更改成功");
    }
    else{
        perror("更换目录失败");
    }

    //second step
    // execute paser,generate syntax_tree.json
    if (system("go run .") == 0){
        printf("运行成功");
    }
    else{
        perror("运行失败");
    }

    //third step
    //execute semantic analyzor,generate var_table.json
    const char * compiler_path = "C:\\Just-For-Fun\\C++\\compiler";
    if (_chdir(compiler_path) == 0){
        printf("更改成功");
    }
    else{
        perror("更换目录失败");
    }

    if(system("C:\\Just-For-Fun\\C++\\compiler\\semantic_analyzor.exe")==0){
        printf("运行成功");
    }
    else{
        perror("运行失败");
    }

    //fourth step
    //execute the object_code generator,generate asm code

    const char *command2 = "python C:\\Just-For-Fun\\C++\\compiler\\object_code_generate.py";
    if (system(command2) == 0){
        printf("执行成功");
    }
    else{
        perror("执行失败");
    }
}