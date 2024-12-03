#include <C:\Program Files\Java\jdk-21\include\jni.h>
#include <iostream>
#include "JNIExample.h"  // 这个头文件是由 javah 或 javac -h 生成的

// 实现本地方法 add
extern "C" JNIEXPORT jint JNICALL
Java_JNIExample_add(JNIEnv *env, jobject obj, jint a, jint b) {
    return a + b;  // 直接返回两个整数的和
}
