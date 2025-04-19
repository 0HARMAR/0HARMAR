package AnnotationTest;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * 校验字符串字段的长度范围
 */
@Target(ElementType.FIELD) // 仅修饰字段
@Retention(RetentionPolicy.RUNTIME) // 运行时保留
public @interface StringLength {
    int min() default 0; // 最小长度，默认0
    int max() default Integer.MAX_VALUE; // 最大长度，默认无限制
    String message() default "字段长度不合法"; // 校验失败提示信息
}