package src.com.example.iocdemo;
import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Map;

public class MyIoCContainer {
    // 存储 Bean 的容器（Key: 类名，Value: 实例）
    private final Map<String, Object> beans = new HashMap<>();

    // 初始化容器时扫描并注册所有标记了 @MyComponent 的类
    public MyIoCContainer(String basePackage) throws Exception {
        // 这里简化为手动注册（真实框架会扫描类路径）
        registerBeans();
        // 依赖注入
        injectDependencies();
    }

    // 手动注册示例 Bean（替代扫描逻辑）
    private void registerBeans() {
        beans.put("userService", new UserService());
        beans.put("userController", new UserController());
    }

    // 依赖注入逻辑：查找所有字段标记了 @MyAutowired 的 Bean，并注入实例
    private void injectDependencies() throws Exception {
        for (Object bean : beans.values()) {
            for (Field field : bean.getClass().getDeclaredFields()) {
                if (field.isAnnotationPresent(MyAutowired.class)) {
                    // 获取字段类型，并查找对应的 Bean 实例
                    Object dependency = beans.get(firstCharToLowerCase(field.getType().getSimpleName()));
                    if (dependency != null) {
                        field.setAccessible(true);
                        // 将依赖注入到当前 Bean 的字段中
                        field.set(bean, dependency);
                    }
                }
            }
        }
    }

    // 从容器中获取 Bean
    public Object getBean(String beanName) {
        return beans.get(beanName);
    }

    public static String firstCharToLowerCase(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        return str.substring(0, 1).toLowerCase() + str.substring(1);
    }
}