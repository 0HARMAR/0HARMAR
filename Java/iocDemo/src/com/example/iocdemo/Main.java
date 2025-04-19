package src.com.example.iocdemo;

public class Main {
    public static void main(String[] args) throws Exception {
        // 初始化 IoC 容器（模拟扫描包）
        MyIoCContainer container = new MyIoCContainer("src.com.example.iocdemo");

        // 从容器中获取 Controller 实例（依赖已自动注入）
        UserController controller = (UserController) container.getBean("userController");
        controller.printUser(); // 输出: User: Alice
    }
}