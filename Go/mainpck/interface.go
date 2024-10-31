package main

type InterfaceName interface {
	Method1() int
	Method2(int) int
	// 可以定义更多的方法...
}

// 定义一个结构体，可以是任何你想要的类型
type MyStruct struct {
}

// MyStruct 结构体实现 InterfaceName 接口的方法
func (ms MyStruct) Method1() int {
	return 1
}

func (ms MyStruct) Method2(x int) int {
	return x + 1
}

func Test() int {
	return 1
}
