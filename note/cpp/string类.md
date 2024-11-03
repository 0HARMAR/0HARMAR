string类的构造函数接受两个迭代器，分别表示构造字符串的起始和终止位置
例如
```cpp
std::string html_content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
```

1. std::istreambuf_iterator<char>(file) 是一个从输入流（file）中读取字符的迭代器，类型是 std::istreambuf_iterator<char>。
2. std::istreambuf_iterator<char>()是默认构造的输入迭代器，用于表示流的末尾。
3. 这段代码会将 file 流中的所有内容读取到字符串 html_content 中