nums := []int{1, 2, 3, 4, 5}
    for index, value := range nums {
        fmt.Println("Index:", index, "Value:", value)
    }

如果不想要Index,可以用_代替

nums := []int{1, 2, 3, 4, 5}
    for _, value := range nums {
        fmt.Println("Index:", index, "Value:", value)
    }