package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	// "bytes"
)

func rtokens() ([][]string, bool) {
	data, err := ioutil.ReadFile("tokens.json")

	STATUS := true

	if err != nil {
		fmt.Println("error when read file : ", err)
		STATUS = false
		return nil, STATUS
	}

	var tokens [][]string

	// 将 JSON 数据解析为切片
	err_slice := json.Unmarshal(data, &tokens)
	if err != nil {
		fmt.Println("Error decoding JSON: ", err_slice)
		STATUS = false
		return nil, STATUS
	}
	return tokens, STATUS
}

// func main() {
// 	data, status := rtokens()

// 	if status {
// 		fmt.Println(data)
// 	}
// }
