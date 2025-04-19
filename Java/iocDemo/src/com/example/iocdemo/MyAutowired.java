package src.com.example.iocdemo;
// 自定义组件注解（模拟 @Component）

import java.lang.annotation.Retention;
import java.lang.annotation.Target;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.ElementType;

// 自定义自动注入注解（模拟 @Autowired）
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface MyAutowired {
}