public class JNIExample {
    // 声明本地方法，native 关键字表示该方法将在 C++ 中实现
    public native int add(int a, int b);

    // 加载本地库
    static {
        System.loadLibrary("native-lib");
    }

    public static void main(String[] args) {
        JNIExample example = new JNIExample();
        int result = example.add(10, 20);
        System.out.println("Result from native code: " + result);
    }
}
