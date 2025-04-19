import cmd

class ScannerConsole(cmd.Cmd):
    prompt = "(vuln-scanner) > "
    
    def __init__(self):
        super().__init__()
        self.current_target = None
    
    def do_scan(self, arg):
        """扫描目标: scan 192.168.1.1"""
        self.current_target = arg
        print(f"开始扫描 {arg}...")
    
    def do_cve(self, arg):
        """执行CVE检测: cve CVE-2021-41773"""
        if not self.current_target:
            print("请先设置目标")
            return
        print(f"检测 {arg}...")
    
    def do_exit(self, arg):
        """退出程序"""
        return True

# 在main()中启动
def main():
    if args.interactive:
        ScannerConsole().cmdloop()