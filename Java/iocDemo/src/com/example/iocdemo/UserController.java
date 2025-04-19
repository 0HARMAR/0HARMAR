package src.com.example.iocdemo;

@MyComponent
public class UserController {
    // 标记需要自动注入的字段
    @MyAutowired
    private UserService userService;

    public void printUser() {
        System.out.println(userService.getUser());
    }
}