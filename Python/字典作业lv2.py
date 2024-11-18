import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def read_words_file(file_path):
    words_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read
            for line in file:
                line = line.strip()
                if line:
                    word, definition = line.split(maxsplit=1)
                    words_dict[word] = definition
    except FileNotFoundError:
        print("文件不存在，将创建一个新文件。")
    return words_dict

def save_words_file(file_path, words_dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, definition in words_dict.items():
            file.write(f"{word} {definition}\n")
def lookup_word():
    word = entry_word.get().strip()
    if not word:
        messagebox.showwarning("警告", "请输入一个单词！")
        return

    definition = words_dict.get(word, None)
    if definition:
        messagebox.showinfo("释义", f"单词 '{word}' 的释义是：{definition}")
    else:
        add_new_word(word)

def add_new_word(word):
    result = messagebox.askyesno("未找到单词", f"单词 '{word}' 不存在，是否要添加？")
    if result:
        definition = simpledialog.askstring("添加释义", f"请输入单词 '{word}' 的释义：")
        if definition:
            words_dict[word] = definition
            save_words_file(file_path, words_dict)
            messagebox.showinfo("成功", f"单词 '{word}' 已成功添加！")
        else:
            messagebox.showwarning("警告", "未输入释义，操作取消。")

file_path = "words.txt"
words_dict = read_words_file(file_path)

window = tk.Tk()
window.title("字典应用")
window.geometry("400x200")

label_instruction = tk.Label(window, text="请输入要查询的单词：")
label_instruction.pack(pady=10)

entry_word = tk.Entry(window, width=30)
entry_word.pack(pady=5)

button_lookup = tk.Button(window, text="查询", command=lookup_word)
button_lookup.pack(pady=10)

window.mainloop()
