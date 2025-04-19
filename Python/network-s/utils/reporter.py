from jinja2 import Template

def generate_html_report(scan_results):
    """生成HTML报告"""
    template_str = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>漏洞扫描报告</title>
        <style>/* 样式代码 */</style>
    </head>
    <body>
        <h1>扫描结果 {{ target }}</h1>
        {% for port in ports %}
        <div class="port">
            <h3>端口 {{ port.port }} ({{ port.service }})</h3>
            <ul>
                {% for vuln in port.vulnerabilities %}
                <li class="critical">{{ vuln }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </body>
    </html>
    """
    
    report = Template(template_str).render(
        target=scan_results['target'],
        ports=scan_results['open_ports']
    )
    
    with open('report.html', 'w') as f:
        f.write(report)