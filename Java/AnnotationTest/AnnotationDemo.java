package AnnotationTest;

public class AnnotationDemo {
    public static void main(String[] args) {
        // 测试用例1：用户名长度不合法
        User user1 = new User("ab", "123456");
        try {
            Validator.validate(user1);
        } catch (Exception e) {
            System.out.println("校验失败: " + e.getMessage());
            // 输出：校验失败: username：用户名长度需在3-20之间 (当前长度: 2)
        }

        // 测试用例2：密码长度不合法
        User user2 = new User("alice", "123");
        try {
            Validator.validate(user2);
        } catch (Exception e) {
            System.out.println("校验失败: " + e.getMessage());
            // 输出：校验失败: password：密码至少6位 (当前长度: 3)
        }

        // 测试用例3：校验通过
        User user3 = new User("alice", "123456");
        try {
            Validator.validate(user3);
            System.out.println("校验通过");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
