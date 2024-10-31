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

func write_to_json(head_data []string, children [][]string) error {
	// 创建根节点切片
	roots := make([]Node, len(head_data))

	// 构建每个根节点及其子节点
	for i, head := range head_data {
		roots[i] = Node{
			Data:     head,
			Children: make([]*Node, len(children[i])),
		}
		for j, child := range children[i] {
			roots[i].Children[j] = &Node{
				Data:     child,
				Children: nil, // 如果没有子节点，设置为 nil
			}
		}
	}

	// 打开或创建 JSON 文件
	file, err := os.Create("syntax_tree.json")
	if err != nil {
		return err
	}
	defer file.Close()

	// 将结构体编码为 JSON 并写入文件
	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")  // 设置缩进格式
	return encoder.Encode(roots) // 将多个根节点编码为 JSON
}
