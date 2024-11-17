#include<iostream>
#include <fstream>
#include <string>
#include "json-develop/single_include/nlohmann/json.hpp"
#include <vector>

using namespace std;
using json = nlohmann::json;

#define PRINT_INFO(desc, x) std::cout << desc << ": " << x << std::endl;
#define PRINT(x) std::cout << x << std::endl;
bool is_interger_string(const string);
template <typename StreamType>
StreamType*
open(string filename){
    StreamType *file = new StreamType(filename);
    if(!file->is_open()){
        cerr << "connot open file tokens.json" << endl;
        return nullptr;
    }
    else{
        return file;
    }
}
    // 定义一个结构体来表示变量
    struct Variable {
        std::string name;  // 变量名称
        std::string type;  // 变量类型
        std::string scope; // 作用域
        int value;  // 值
};

json create_var_table_json(std::map<string,std::vector<Variable>> func_name_with_var_table){
    json var_table_json;
    for (const auto& fnwvt : func_name_with_var_table){
        string func_name = fnwvt.first;
        vector<Variable> var_table = fnwvt.second;
        cout << "写入json:" << func_name << endl;
        for(const auto& var : var_table){
        var_table_json[func_name].push_back({
            {"name",var.name},
            {"type",var.type},
            {"scope",var.scope},
            {"value",var.value},
        });
    }
    }
    return var_table_json;
}

map<string,vector<Variable>> generate_var_table(json json_obj){
    map<string,vector<Variable>> func_name_with_var_table;
    // traverse per function
    for (auto &func : json_obj.items()){
         // now we get the func_name
        string func_name = func.key();
        vector<vector<string>> func_tokens = func.value();
        vector <Variable> var_table;
        for(int i=0;i < func_tokens.size();i++){
            vector <string> line = func_tokens[i];
            Variable var;
            if (line[0] == "int"){
                var.type = "int";
                var.name = line[1];
                var.scope = "global";
                if (is_interger_string(line[3])){
                    var.value = stoi(line[3]);
                }
                var_table.push_back(var);
        }
    }
    // now we get the vector<Variable> var_table
    func_name_with_var_table[func_name] = var_table;
}
    return func_name_with_var_table;
}

// judge is a number string
bool is_interger_string(const string str){
    try{
        int num = stoi(str);
        return true;
    }
    catch(...){
        return false;
    }
}
// print file stream
void pfstream(ifstream infile){
    string line;
    while(getline(infile,line)){
        PRINT(line)
    }
}

void seekStart(ifstream infile){
    // seek to file start
    infile.clear();
    infile.seekg(0,ios::beg);
}

// print json obj
void pJson(json json_obj){
    PRINT("print the json file according to elements")
    for(int i=0;i < json_obj.size();i++){
        PRINT(json_obj[i])
    }
}

// print var table
void pVarTable(vector<Variable> var_table){
    for (const auto& var : var_table) {
        std::cout << "Name: " << var.name 
                  << ", Type: " << var.type 
                  << ", Scope: " << var.scope 
                  << ", Value: " << var.value << std::endl;
    }
}
int main(){
    ifstream *infile = nullptr;
    cout << "Please enter the file name: ";
    infile = open<ifstream>("go_used/tokens_func.json");
    if (infile == nullptr) {
        throw runtime_error("cannot open file");
    }
    cout << "open file tokens_func.json" << endl;
    json json_obj;
    *infile >> json_obj;
    if (infile->good()) {
        cout << "read good" << endl;
    }
    json var_table_json = create_var_table_json(generate_var_table(json_obj));
    ofstream *ofile = open<ofstream>("var_table.json");

    if (ofile != nullptr) {
        *ofile << var_table_json.dump(4);

        ofile->close();
    }
    else {
        cout << "open file error." << endl;
    }
    return 0;
}
