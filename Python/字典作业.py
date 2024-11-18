def read_words_file(file_path):
    words_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    word, definition = line.split(maxsplit=1)
                    words_dict[word] = definition
    except FileNotFoundError:
        print("文件不存在，将创建一个新文件。")
    return words_dict

def lookup_word(word, words_dict):
    return words_dict.get(word, None)

def add_word(word, definition, words_dict):
    words_dict[word] = definition

def save_words_file(file_path, words_dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, definition in words_dict.items():
            file.write(f"{word} {definition}\n")

def main():
    file_path = "Python/words.txt"
    words_dict = read_words_file(file_path)
    
    while True:
        user_input = input("\n请输入要查找的单词（输入'退出'结束程序）：").strip()
        if user_input == "退出":
            print("再见")
            break
        
        definition = lookup_word(user_input, words_dict)
        if definition:
            print(f"单词 '{user_input}' 的释义是：{definition}")
        else:
            print(f"单词 '{user_input}' 不存在！")
            choice = input("是否需要添加该单词及其释义到字典中？(y/n): ").strip().lower()
            if choice == 'y':
                new_definition = input(f"请输入单词 '{user_input}' 的释义：").strip()
                add_word(user_input, new_definition, words_dict)
                save_words_file(file_path, words_dict)
                print(f"单词 '{user_input}' 已添加并保存到文件中。")
            else:
                print("未添加该单词。")

if __name__ == "__main__":
    main()
