def check_cve_vulnerabilities(target_url, service, version):
    """基于CVE数据库检测漏洞"""
    with open('cve_db.json') as f:
        cve_db = json.load(f)
    
    for entry in cve_db:
        if service.lower() in entry['cve_id'].lower():
            if is_affected(version, entry['affected_versions']):
                print(f"[!] 发现 {entry['cve_id']}: {entry['description']}")
                if 'test_paths' in entry:
                    test_paths(target_url, entry['test_paths'])