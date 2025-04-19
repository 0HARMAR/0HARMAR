package AnnotationTest;

public class User {
    @StringLength(min = 3, max = 20, message = "用户名长度需在3-20之间")
    private String username;

    @StringLength(min = 6, message = "密码至少6位")
    private String password;

    // 构造方法
    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // Getter/Setter (省略)
}