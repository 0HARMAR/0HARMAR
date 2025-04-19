import nmap
import requests
import argparse
from colorama import Fore, init
import os
from datetime import datetime

# 初始化颜色输出
init(autoreset=True)

# 全局变量存储扫描结果
scan_results = {
    'ports': [],
    'vulns': [],
    'target': '',
    'scan_time': ''
}

def generate_html_report():
    """生成HTML报告"""
    # 创建报告目录
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # 文件名格式：目标IP_时间戳.html
    filename = f"{scan_results['target']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    filepath = os.path.join(report_dir, filename)
    
    # HTML内容生成
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>漏洞扫描报告 - {scan_results['target']}</title>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; border-bottom: 2px solid #333; }}
            .summary {{ margin: 20px 0; padding: 10px; background: #f0f0f0; }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            .vuln-critical {{ color: #ff0000; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>漏洞扫描报告 - {scan_results['target']}</h1>
        <div class="summary">
            扫描时间: {scan_results['scan_time']}<br>
            开放端口数: {len(scan_results['ports'])}<br>
            发现漏洞数: {len(scan_results['vulns'])}
        </div>
        
        <h2>端口扫描结果</h2>
        <table>
            <tr>
                <th>端口</th>
                <th>服务</th>
                <th>软件</th>
                <th>版本</th>
            </tr>
            {"".join(f'<tr><td>{p["port"]}</td><td>{p["service"]}</td><td>{p["product"]}</td><td>{p["version"]}</td></tr>' for p in scan_results['ports'])}
        </table>
        
        <h2>漏洞列表</h2>
        <table>
            <tr>
                <th>类型</th>
                <th>详情</th>
            </tr>
            {"".join(f'<tr><td class="vuln-critical">{v["type"]}</td><td>{v["details"]}</td></tr>' for v in scan_results['vulns'])}
        </table>
    </body>
    </html>
    """
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(Fore.GREEN + f"\n[+] 报告已生成: {os.path.abspath(filepath)}")

def port_scan(target_ip):
    """使用Nmap进行端口扫描和服务识别"""
    try:
        print(Fore.CYAN + f"\n[+] 正在扫描目标 {target_ip} 的开放端口...")
        scanner = nmap.PortScanner()
        scanner.scan(target_ip, arguments='-p 1-1000 -sV --version-light -O')
        
        for host in scanner.all_hosts():
            print(Fore.GREEN + f"\n[+] 主机: {host}")
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    service = scanner[host][proto][port]['name']
                    product = scanner[host][proto][port].get('product', '未知')
                    version = scanner[host][proto][port].get('version', '未知')
                    # 记录端口信息
                    scan_results['ports'].append({
                        'port': port,
                        'service': service,
                        'product': product,
                        'version': version
                    })
                    print(f"端口: {port}\t服务: {service}\t软件: {product} {version}")
    except Exception as e:
        print(Fore.RED + f"[-] 扫描失败: {str(e)}")

def check_web_vulns(target_url):
    """检测Web常见漏洞"""
    print(Fore.CYAN + f"\n[+] 正在检测 {target_url} 的Web漏洞...")
    
    # 检测SQL注入
    sql_payloads = ["'", "1' OR '1'='1", "1' SLEEP(5)--"]
    for payload in sql_payloads:
        try:
            test_url = f"{target_url}?id={payload}"
            response = requests.get(test_url, timeout=5)
            if "error" in response.text.lower() or "syntax" in response.text.lower():
                vuln_info = f"SQL注入漏洞: {test_url}"
                print(Fore.RED + f"[!] 发现{vuln_info}")
                scan_results['vulns'].append({
                    'type': 'SQL注入',
                    'details': vuln_info
                })
                return
        except requests.exceptions.Timeout:
            vuln_info = f"基于时间的SQL注入: {payload}"
            print(Fore.YELLOW + f"[!] {vuln_info}")
            scan_results['vulns'].append({
                'type': 'SQL注入',
                'details': vuln_info
            })
        except Exception as e:
            pass
    
    # 检测目录遍历（示例）
    traversal_paths = ["../../etc/passwd", "wp-admin.php"]
    for path in traversal_paths:
        test_url = f"{target_url}/{path}"
        response = requests.get(test_url)
        if "root:" in response.text or "WordPress" in response.text:
            vuln_info = f"目录遍历漏洞: {test_url}"
            print(Fore.RED + f"[!] 发现{vuln_info}")
            scan_results['vulns'].append({
                'type': '目录遍历',
                'details': vuln_info
            })
    
    print(Fore.GREEN + "[+] 基础Web漏洞检测完成")

def main():
    # 初始化全局变量
    global scan_results
    scan_results = {'ports': [], 'vulns': [], 'target': '', 'scan_time': ''}
    
    parser = argparse.ArgumentParser(
        description="简易漏洞扫描器 - 作者: 网络安全助手",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-t", "--target", help="目标IP地址", required=True)
    parser.add_argument("-w", "--web", help="启用Web漏洞扫描", action="store_true")
    args = parser.parse_args()

    scan_results['target'] = args.target
    scan_results['scan_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(Fore.BLUE + "\n" + "="*40)
    print(Fore.YELLOW + "简易漏洞扫描器启动")
    print(Fore.BLUE + "="*40)
    
    # 执行端口扫描
    port_scan(args.target)
    
    # 执行Web漏洞扫描
    if args.web:
        check_web_vulns(f"http://{args.target}:81")
    
    # 生成HTML报告
    generate_html_report()

if __name__ == "__main__":
    main()