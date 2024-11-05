1. 使用计数器
```go
n := 5
    for i := 0; i < n; i++ {
        fmt.Println("Iteration:", i+1)
    }
```
2. 空for循环
```go
count := 0
    n := 5
    for count < n {
        fmt.Println("Iteration:", count+1)
        count++
    }
```
3. 使用range
```go
 n := 5
    for i := range make([]struct{}, n) {
        fmt.Println("Iteration:", i+1)
    }
```
如果不需要使用i变量，可以直接
```go
 n := 5
    for range make([]struct{}, n) {
        //body
    }
```