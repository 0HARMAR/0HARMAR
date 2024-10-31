package main

func RET0() int {
	defer println("func RET0 over")
	return 0
}
