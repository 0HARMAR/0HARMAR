package AnnotationTest;

import java.lang.reflect.Field;

/**
 * 校验工具类：检查字段是否符合 @StringLength 规则
 */
public class Validator {
    public static void validate(Object obj) throws IllegalArgumentException, IllegalAccessException {
        Class<?> clazz = obj.getClass();
        // 遍历所有字段
        for (Field field : clazz.getDeclaredFields()) {
            // 检查字段是否有 @StringLength 注解
            if (field.isAnnotationPresent(StringLength.class)) {
                field.setAccessible(true); // 允许访问私有字段
                String value = (String) field.get(obj); // 获取字段值
                StringLength annotation = field.getAnnotation(StringLength.class);
                
                // 校验逻辑
                if (value == null) {
                    throw new IllegalArgumentException(field.getName() + "：" + annotation.message());
                }
                int length = value.length();
                if (length < annotation.min() || length > annotation.max()) {
                    String errorMsg = String.format("%s：%s (当前长度: %d)", 
                        field.getName(), annotation.message(), length);
                    throw new IllegalArgumentException(errorMsg);
                }
            }
        }
    }
}
