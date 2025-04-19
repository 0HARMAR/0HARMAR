package main

import (
	"encoding/json"
	"fmt"
	"os"
	"sync"
)

// Node 表示语法树节点
type Node struct {
	Data     string  `json:"data"`
	Children []*Node `json:"children,omitempty"`
}

// FunctionAST 函数抽象语法树结构
type FunctionAST struct {
	Name string
	Tree []Node
}

// 常量定义
const (
	FuncToken = "func"
	TabIndent = "\t"
)

// CountFunctionDeclarations 统计函数声明数量（优化内存分配[1,4](@ref)）
func CountFunctionDeclarations(data [][]string) int {
	count := 1 // 包含main函数
	for _, line := range data {
		if len(line) > 0 && line[0] == FuncToken {
			count++
		}
	}
	return count
}

// SplitByFunctionScope 按函数作用域分割代码（预分配内存[4](@ref)）
func SplitByFunctionScope(data [][]string) (mainTokens [][]string, funcIndex map[string][2]int, err error) {
	funcIndex = make(map[string][2]int)
	currentFunc := "main"
	startIndex := 0

	for i, line := range data {
		if len(line) == 0 {
			continue
		}

		switch line[0] {
		case FuncToken:
			if len(line) < 2 {
				return nil, nil, fmt.Errorf("函数定义错误 at line %d", i+1)
			}
			currentFunc = line[1]
			startIndex = i
		case TabIndent:
			if i+1 < len(data) && data[i+1][0] != TabIndent {
				funcIndex[currentFunc] = [2]int{startIndex, i}
			}
		default:
			mainTokens = append(mainTokens, line)
		}
	}
	return
}

// ResolveExpressionTree 解析表达式树（优化循环逻辑[3,6](@ref)）
func ResolveExpressionTree(tokens [][]string) []Node {
	nodes := make([]Node, 0, len(tokens))
	
	for _, line := range tokens {
		var destVar string
		operands := make([]string, 0, 3)
		
		for i, token := range line {
			switch token {
			case "=":
				if i > 0 {
					destVar = line[i-1]
				}
			case "+":
				if i > 0 {
					operands = append(operands, line[i-1])
				}
			}
		}
		
		if len(line) > 0 {
			operands = append(operands, line[len(line)-1])
		}

		if destVar != "" {
			node := Node{Data: destVar}
			for _, op := range operands {
				node.Children = append(node.Children, &Node{Data: op})
			}
			nodes = append(nodes, node)
		}
	}
	return nodes
}

// GenerateSyntaxTree 生成完整语法树（并发优化[2,8](@ref)）
func GenerateSyntaxTree(data [][]string) (map[string][]Node, error) {
	mainTokens, funcIndex, err := SplitByFunctionScope(data)
	if err != nil {
		return nil, err
	}

	result := make(map[string][]Node)
	var wg sync.WaitGroup
	resultChan := make(chan FunctionAST, 10)

	// 处理main函数
	wg.Add(1)
	go func() {
		defer wg.Done()
		resultChan <- FunctionAST{
			Name: "main",
			Tree: ResolveExpressionTree(mainTokens),
		}
	}()

	// 并发处理其他函数
	for name, bounds := range funcIndex {
		if name == "main" {
			continue
		}

		wg.Add(1)
		go func(name string, start, end int) {
			defer wg.Done()
			funcTokens := make([][]string, 0, end-start+1)
			for i := start; i <= end; i++ {
				funcTokens = append(funcTokens, data[i])
			}
			resultChan <- FunctionAST{
				Name: name,
				Tree: ResolveExpressionTree(funcTokens),
			}
		}(name, bounds[0], bounds[1])
	}

	// 结果收集
	go func() {
		wg.Wait()
		close(resultChan)
	}()

	for ast := range resultChan {
		result[ast.Name] = ast.Tree
	}

	return result, nil
}

// WriteToJSON 写入JSON文件（错误处理优化[5,7](@ref)）
func WriteToJSON(data interface{}, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("文件创建失败: %w", err)
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	if err := encoder.Encode(data); err != nil {
		return fmt.Errorf("JSON编码失败: %w", err)
	}
	return nil
}

func main() {
	data, err := ReadTokens()
	if err != nil {
		fmt.Printf("错误: %v\n", err)
		return
	}

	// 生成语法树
	ast, err := GenerateSyntaxTree(data)
	if err != nil {
		fmt.Printf("语法解析错误: %v\n", err)
		return
	}

	// 写入JSON
	if err := WriteToJSON(ast, "ast_output.json"); err != nil {
		fmt.Printf("写入失败: %v\n", err)
	}
}