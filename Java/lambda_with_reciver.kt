fun MyLayout(content: () -> Unit) {
    content()  // 调用 lambda
}

fun main() {
    MyLayout {
        println("Hello from inside the layout!")
        println("next sentence")
    }
}
