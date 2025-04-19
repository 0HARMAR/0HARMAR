package src.com.example.iocdemo;
// 标记为组件（会被容器管理）

@MyComponent
public class UserService {
    public String getUser() {
        return "User: Alice";
    }
}