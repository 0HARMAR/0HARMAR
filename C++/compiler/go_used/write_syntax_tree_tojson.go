package main

import (
	"encoding/json"
	//"io/ioutil"
	"os"
)

// 定义节点结构体
type Node struct {
	Data     string  `json:"data"`
	Children []*Node `json:"children"`
}

func write_to_json(functions map[string][]Node) error {
	// 打开或创建 JSON 文件
	file, err := os.Create("syntax_tree.json")
	if err != nil {
		return err
	}
	defer file.Close()

	// 将结构体编码为 JSON 并写入文件
	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")      // 设置缩进格式
	return encoder.Encode(functions) // 将多个根节点编码为 JSON
}
