#include<iostream>
#include <fstream>
#include <string>
#include "json-develop\single_include\nlohmann\json.hpp"
#include <vector>

using namespace std;
using json = nlohmann::json;

#define PRINT_INFO(desc, x) std::cout << desc << ": " << x << std::endl;
#define PRINT(x) std::cout << x << std::endl;

string var_name = ""; // var name table

// 定义一个结构体来表示变量
struct Variable {
    std::string name;  // 变量名称
    std::string type;  // 变量类型
    std::string scope; // 作用域
    int value;  // 值
};

json create_var_table(const vector<Variable>& table){
    json var_table;
    for(const auto& var : table){
        var_table["var"].push_back({
            {"name",var.name},
            {"type",var.type},
            {"scope",var.scope},
            {"value",var.value},
        });
    }
    return var_table;
}


int main(){
    ifstream infile("go_used/tokens.json");
    if(!infile.is_open()){
        cerr << "connot open file tokens.json" << endl;
        return 1;
    }

    string line;
    while(getline(infile,line)){
        PRINT(line)
    }

    // seek to file start
    infile.clear();
    infile.seekg(0,ios::beg);

    json json_obj;
    infile >> json_obj;

    PRINT("print the json file according to elements")
    for(int i=0;i < json_obj.size();i++){
        PRINT(json_obj[i])
    }

    // create var table json file

    vector <Variable> var_table;
    for(int i=0;i < json_obj.size();i++){
        vector <string> line = json_obj[i];
        Variable var;
        if (line[0] == "int"){
            var.type = "int";
            var.name = line[1];
            var.scope = "global";
            var.value = stoi(line[3]);
            var_name += var.name;
            var_table.push_back(var);
        }
    }
    // 打印验证
    for (const auto& var : var_table) {
        std::cout << "Name: " << var.name 
                  << ", Type: " << var.type 
                  << ", Scope: " << var.scope 
                  << ", Value: " << var.value << std::endl;
    }

    json var_table_ = create_var_table(var_table);
    ofstream ofile("var_table.json");
    if(!ofile.is_open()){
        cerr << "connot open file var_table.json" << endl;
        return 1;
    }

    ofile << var_table_.dump(4);

    ofile.close();

    return 0;
}
// create var table


//analyze syntax tree
