hwnd = win32gui.FindWindow("ConsoleWindowClass", None) # 根据窗口标题获取句柄
text = win32gui.GetWindowText(hwnd)
print(text)
controls = []
win32gui.EnumChildWindows(hwnd, callback, controls)

for control in controls:
	button_text = win32gui.GetWindowText(control)
	print(button_text)