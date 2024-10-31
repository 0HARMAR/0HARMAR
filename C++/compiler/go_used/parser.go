package main

import (
	"fmt"
)

func main() {
	//first step
	//read tokens,divide the code by function

	//second step
	//use paser for the each functions
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
