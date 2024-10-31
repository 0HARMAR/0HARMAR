package main

import (
	"fmt"
	"sync"
)

var SUM = 0

const (
	N = 100000
)

func PRINT() int {
	defer fmt.Println("func over")
	fmt.Println("hello")
	return 1
}

func sum(wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 0; i < N; i++ {
		SUM++
	}
}

func main() {
	// println("return 0 :", RET0())
	// person := Person{"hmy", 18}
	// person.Setname("hemingyang")
	// println(person.name)
	// Printstc()
	// var wg sync.WaitGroup
	// wg.Add(2)
	// go sum(&wg)
	// go sum(&wg)

	// fmt.Println("hello user 1")

	// wg.Wait()

	// println("sum : ", SUM)
	// PRINT()

	c := make(chan int)

	go func() {
		defer fmt.Println("func over!")

		fmt.Println("func running")

		c <- 1

	}()

	// if not fetch value from channel,goroutine will block
	// and the 'func over' will not be print

	fmt.Println("main goroutine running")

	// infinite loop
	// for {
	// }

	receive := <-c

	//println(receive)
}
