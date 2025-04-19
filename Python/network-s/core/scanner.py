import concurrent.futures
import cmd
import nmap

def fast_port_scan(target_ip, ports="1-1000", threads=50):
    """多线程端口扫描"""
    open_ports = []
    scanner = nmap.PortScanner()
    
    # 使用线程池执行扫描任务
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for port in parse_port_range(ports):  # 自定义端口解析函数
            futures.append(
                executor.submit(
                    scanner.scan,
                    target_ip,
                    str(port),
                    arguments="-sV --version-light"
                )
            )
        
        # 收集结果
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                for host in result.all_hosts():
                    for proto in result[host].all_protocols():
                        ports = result[host][proto]
                        for port, data in ports.items():
                            if data['state'] == 'open':
                                open_ports.append({
                                    'port': port,
                                    'service': data['name'],
                                    'version': data.get('product', '')
                                })
            except Exception as e:
                print(f"扫描错误: {str(e)}")
    return open_ports

import argparse

class ScannerConsole(cmd.Cmd):
    prompt = "(vuln-scanner) > "
    
    def __init__(self):
        super().__init__()
        self.current_target = None  # 目标在交互模式中动态设置

    def do_set(self, arg):
        """设置目标或参数: set target 192.168.1.1"""
        if not arg.startswith("target"):
            print("Usage: set target <IP>")
            return
        self.current_target = arg.split()[-1]
        print(f"[+] 目标已设置为 {self.current_target}")

    def do_scan(self, arg):
        """执行扫描任务: scan --ports 80,443"""
        if not self.current_target:
            print("[-] 请先使用 'set target <IP>' 指定目标")
            return
        print(f"[*] 开始扫描 {self.current_target}...")
        # 调用扫描逻辑

    def do_exit(self, arg):
        """退出程序"""
        return True
    
def main():
    parser = argparse.ArgumentParser(description="漏洞扫描器")
    parser.add_argument("-t", "--target", required=False, help="扫描目标IP或域名")  # 改为非必须
    parser.add_argument("--interactive", action="store_true", help="进入交互模式")
    # 其他参数保持不变...
    args = parser.parse_args()

    # 添加逻辑校验
    if not args.interactive and not args.target:
        parser.error("非交互模式必须使用 -t/--target 指定目标")
    
    if args.interactive:
        ScannerConsole().cmdloop()
    else:
        start_scanning(args.target, ...)

if __name__ == "__main__":
    main()