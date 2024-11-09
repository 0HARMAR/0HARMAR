package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func get_func_num(data [][]string) int {
	func_num := 1
	data, status := rtokens()
	if status {
		for _, line := range data {
			if line[0] == "func" {
				func_num += 1
			}
		}
	}
	return func_num
}

func print_tokens(data [][]string) {
	for index, value := range data {
		fmt.Printf("第%d行 :", index)
		fmt.Println(value)
	}
}

// accept one file tokens
// divide the tokens according to
// functions ,ruturn slice of [][]string
func divide_by_function(data [][]string) ([][]string, map[string]map[int]int) {
	var func_index map[string]map[int]int
	func_index = make(map[string]map[int]int)
	func_index["main"] = map[int]int{
		0: len(data),
	}
	var main [][]string
	var current_func_name string = "main"
	var current_func_start_index int = 0
	for index, line := range data {
		if line[0] != "func" && line[0] != "\t" {
			main = append(main, line)
		} else if line[0] == "func" {
			current_func_name = line[1]
			current_func_start_index = index + 1
		} else if line[0] == "\t" {
			// data[index + 1] is next line
			if data[index+1][0] != "\t" {
				func_index[current_func_name] = map[int]int{
					current_func_start_index: index,
				}
			}
		}
	}
	fmt.Println(main)
	return main, func_index
}

// accept one function's tokens
// and resolve the express in this
// function ,rutun the []Node
// per Node represents a express
// []Node reprensents a func's express

func resolve_express_func(tokens [][]string) []Node {
	var expresses [][]string
	for i := 0; i < len(tokens); i++ {
		data_line := tokens[i]
		fmt.Println("token 数:", len(data_line))
		for j := 0; j < len(data_line); j++ {
			if data_line[j] == "+" { // if line has '+',it is a express
				expresses = append(expresses, data_line)
				break
			}
		}
	}
	fmt.Println("总的表达式")
	for i := 0; i < len(expresses); i++ { // print the express
		fmt.Println(expresses[i])
	}

	var dest_var []string                       // slice of distination varible
	operand := make([][]string, len(expresses)) // slice of dest_var operand
	for index, express := range expresses {
		operand[index] = make([]string, 0)
		// found left value
		for index_ := 0; index_ < len(express); index_++ {
			if express[index_] == "=" {
				dest_var = append(dest_var, express[index_-1])
			}
		}
		count := 0
		for j := 0; j < len(express); j++ { //count '+' num
			if express[j] == "+" {
				count += 1
			}
		}
		fmt.Println(count)
		for j := 0; j < len(express); j++ {
			if express[j] == "+" {
				op1 := express[j-1]
				operand[index] = append(operand[index], op1)
			}
		}
		operand[index] = append(operand[index], express[len(express)-1])
		fmt.Println(operand)
	}

	// now we have dest_var and
	// oprand , and transform to
	// struct []Node

	var Nodes []Node
	for i := 0; i < len(dest_var); i++ {
		var node Node // head node
		node.Data = dest_var[i]
		for j := 0; j < len(operand[i]); j++ {
			// child node
			node_ := Node{
				Data:     operand[i][j],
				Children: nil,
			}
			node.Children = append(node.Children, &node_)
		}

		Nodes = append(Nodes, node)
	}
	return Nodes
}

func generate_func_tokens(func_name string,
	func_index map[string]map[int]int,
	data [][]string) [][]string {
	var start int
	var end int
	for key, value := range func_index[func_name] {
		start = key
		end = value
	}

	var func_tokens [][]string = [][]string{}
	for i := range make([]struct{}, end-start+1) {
		func_tokens = append(func_tokens, data[start+i])
	}

	return func_tokens
}

// accept all function's resolved syntax
// tree, generate the final syntax tree
func generate_syntax_tree(data [][]string) {
	main, func_index := divide_by_function(data)
	func_num := get_func_num(data)
	var func_syntax_tree map[string][]Node = make(map[string][]Node)
	fmt.Println(main)
	for key, value := range func_index {
		fmt.Println("函数名 : ", key)
		for key_, value_ := range value {
			fmt.Println("start : ", key_)
			fmt.Println("end : ", value_)
		}
	}
	fmt.Print(func_index["main"])

	for range make([]struct{}, func_num) {
		for key, value := range func_index {
			if key == "main" {
				func_syntax_tree["main"] = resolve_express_func(main)
			} else {
				func_name := key
				func_tokens := generate_func_tokens(func_name, func_index, data)
				func_syntax_tree[func_name] = resolve_express_func(func_tokens)
			}
			for key_, value_ := range value {
				fmt.Println("start : ", key_)
				fmt.Println("end : ", value_)
			}
		}
	}

	// now we get the func_syntax_tree
	// with type map[string](func_name)[]Node(
	// func syntax tree)

	write_to_json(func_syntax_tree)
}

func write_per_func_tokens_toJson(data [][]string) {
	var jsonDate map[string][][]string = make(map[string][][]string)
	main, func_index := divide_by_function(data)

	for key, _ := range func_index {
		if key == "main" {
			jsonDate["main"] = main
		} else {
			func_name := key
			func_tokens := generate_func_tokens(func_name, func_index, data)
			jsonDate[func_name] = func_tokens
		}
	}

	file, err := os.Create("tokens_func.json")
	if err != nil {
		fmt.Println("无法创建文件:", err)
		return
	}
	defer file.Close()

	// 将结构体编码为 JSON 并写入文件
	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ") // 设置缩进格式
	if err := encoder.Encode(jsonDate); err != nil {
		fmt.Println("JSON 编码失败:", err)
	}
}

func main() {
	//first step
	//read tokens,divide the code by function

	//second step
	//use paser for the each functions

	data, status := rtokens()
	if status {
		write_per_func_tokens_toJson(data)
	}
}
