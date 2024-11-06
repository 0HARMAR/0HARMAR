1. 定义
```go
var m map[keyType]valueType
```
2. 初始化
```go
// 用make初始化
ages := make(map[string]int)

// 用字面量初始化
ages := map[string]int{
    "Alice": 30,
    "Bob":   25,
}
```
3. 遍历
```go
// 定义一个 map
	myMap := map[string]int{
		"apple":  3,
		"banana": 5,
		"cherry": 7,
	}

	// 遍历 map
	for key, value := range myMap {
		fmt.Printf("键: %s, 值: %d\n", key, value)
	}
```
