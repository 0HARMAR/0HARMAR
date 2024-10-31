# print_regs.py
import gdb

class PrintRegs(gdb.Command):
    def __init__(self):
        super(PrintRegs, self).__init__("print_regs", gdb.COMMAND_USER)
        self.last_cmd = None

    def invoke(self, arg, from_tty):
        # Print the registers
        gdb.execute("info registers")

# Register the command
PrintRegs()

class RegisterHooks(gdb.Command):
    def __init__(self):
        super(RegisterHooks, self).__init__("register_hooks", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        gdb.execute("define hook-step")
        gdb.execute("print_regs")
        gdb.execute("end")

# Register the hooks command
RegisterHooks()

