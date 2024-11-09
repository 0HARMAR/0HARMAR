**导入encoding/json包**

```go
// 创建一个结构体实例
	person := Person{
		Name:  "Alice",
		Age:   30,
		Email: "alice@example.com",
	}

	// 打开文件，如果文件不存在则创建
	file, err := os.Create("person.json")
	if err != nil {
		fmt.Println("无法创建文件:", err)
		return
	}
	defer file.Close()

	// 将结构体编码为 JSON 并写入文件
	encoder := json.NewEncoder(file)
    encoder.SetIndent("", "  ")      // 设置缩进格式
	if err := encoder.Encode(person); err != nil {
		fmt.Println("JSON 编码失败:", err)
	}
```

