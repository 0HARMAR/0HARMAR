using System;

public class MyClass {
    public int MyProperty { get; set; }

    public void MyMethod() {
        Console.WriteLine("Hello from MyMethod!");
    }
}

public class Program {
    public static void Main() {
        Type type = typeof(MyClass);
        Console.WriteLine("Type Name: " + type.Name);
        Console.WriteLine("Namespace: " + type.Namespace);
        
        // 获取所有属性
        var properties = type.GetProperties();
        foreach (var property in properties) {
            Console.WriteLine("Property: " + property.Name);
        }

        // 获取所有方法
        var methods = type.GetMethods();
        foreach (var method in methods) {
            Console.WriteLine("Method: " + method.Name);
        }
    }
}
