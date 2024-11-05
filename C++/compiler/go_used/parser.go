package main

import (
	"fmt"
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

// accept one file tokens
// divide the tokens according to
// functions ,ruturn slice of [][]string
func divide_by_function(data [][]string) [][][]string {
	var func_index map[string]map[int]int
	func_index["main"] = map[int]int{
		0: len(data),
	}
	func_num := get_func_num(data)
	var main [][]string
	var is_in_main bool = true
	var current_func_name string = "main"
	var current_func_start_index int = 0
	for index, line := range data {
		is_in_main = true
		if line[0] != "func" && line[0] != "\t" {
			main = append(main, line)
		} else if line[0] == "func" {
			is_in_main = false
			current_func_name = line[1]
			current_func_start_index = index
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

	for range make([]struct{}, func_num-1) {

	}
	return [][][]string{}
}

// accept one function's tokens
// and resolve the express in this
// function ,rutun the result
func resolve_express_func(tokens [][]string) {

}

// accept all function's resolved syntax
// tree, generate the final syntax tree
func generate_syntax_tree() {
	data, status := rtokens()
	if status {
		var expresses [][]string
		for i := 0; i < len(data); i++ {
			data_line := data[i]
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

		var dest_var []string
		operand := make([][]string, len(expresses))
		for index, express := range expresses {
			operand[index] = make([]string, 0)
			dest_var = append(dest_var, express[0])
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

		write_to_json(dest_var, operand)
	}
}

func main() {
	//first step
	//read tokens,divide the code by function

	//second step
	//use paser for the each functions

	data, status := rtokens()
	if status {
		func_num := get_func_num(data)
		fmt.Println(func_num)
	}

	divide_by_function(data)
}
