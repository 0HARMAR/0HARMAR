package main

type Person struct {
	name string
	age  int
}

func (this *Person) Setname(name string) {
	this.name = name
}

func Printstc() {
	person := Person{"hmy", 18}
	println("name is, ", person.name, "age is", person.age)
}
