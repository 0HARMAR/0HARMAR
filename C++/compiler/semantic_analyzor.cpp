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

int get_func_name_index(vector <string> line){
    for (auto it = line.begin(); it != line.end(); ++it) {
        size_t index = std::distance(line.begin(), it);// 获取迭代的Index
        if (*it == "int"){
            return index+1;
        }
    }

    return -1;
}
// judge a line is a var decalre
// and process the var declare
// line,such as
// 'int a','int a = 5'
// 'int a = b + c'
// return is/not a var decalre
// and func name ,init value throgh reference
bool process_var_declare(vector<string> line,string &func_name,string &init_value){
    for(auto it = line.begin();it !=line.end();++it){
        size_t index = distance(line.begin(),it);
        if (*it == "int"){
            func_name = line[index+1];
             for(auto it_ = next(it);it_ != line.end(); ++it_){
                size_t index_ = distance(line.begin(),it_);
                if (*it_ == "="){
                    // line[index_+1] is init value,if exist
                    // if init value is const
                    if (is_interger_string(line[index_+1]))
                    {
                        init_value = line[index_+1];
                    }
                    // init value is operate of other vars
                    else{
                        // generate the init express
                        string express = "";
                        for (auto it__ = next(it_);it__!=line.end();++it__){
                            size_t index__ = distance(line.begin(),it__);
                            express += *it__;
                        }

                        init_value = express;
                    }
                }
            }
        }
    }
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
            int func_name_index = get_func_name_index(line);
            var.type = "int";
            if (func_name_index!=-1){
                    var.name = line[func_name_index];
            }
            if (line[0] == "\t"){
                var.scope = func_name + "_local";
                if (is_interger_string(line[4])){
                    var.value = stoi(line[4]);
                }
                var_table.push_back(var);
            }
            else if (line[0] == "int"){
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
