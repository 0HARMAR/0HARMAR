import gdb

class TraceFunctionCalls(gdb.Command):
    def __init__(self):
        super(TraceFunctionCalls, self).__init__("trace-calls", gdb.COMMAND_USER)
        self.function_addresses = {}

    def invoke(self, arg, from_tty):
        gdb.events.call.connect(self.on_call)
        gdb.events.exited.connect(self.on_exit)
        print("Started tracing function calls...")

    def on_call(self, event):
        # 获取当前调用栈帧
        frame = gdb.selected_frame()
        # 获取函数名称
        function_name = frame.name()
        # 获取函数起始地址
        function_address = frame.pc()

        if function_name:
            if function_name not in self.function_addresses:
                self.function_addresses[function_name] = function_address
                print(f"Function: {function_name}, Address: {function_address:#x}")

    def on_exit(self, event):
        print("Process exited, stopping trace.")
        gdb.events.call.disconnect(self.on_call)
        gdb.events.exited.disconnect(self.on_exit)

# 注册命令
TraceFunctionCalls()
