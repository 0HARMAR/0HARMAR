package main

import (
	."C:\\Just-For-Fun\\Go\\main1"
	"fmt"
	"time"
)

const (
	OK = 1
)

func main() {
	fmt.Println("Hello, World!")
	print("im arg")
	fmt.Printf("return value %d", Test())
	go spinner(100 * time.Millisecond)
	const n = 45
	fibN := fib(n) // slow
	fmt.Printf("\rFibonacci(%d) = %d\n", n, fibN)
}

func print(x string) int {
	fmt.Printf("%s", x)
	return OK
}
