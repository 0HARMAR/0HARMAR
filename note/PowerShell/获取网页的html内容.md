使用 Invoke-WebRequest -Uri "https://www.example.com" 命令

还可以用一个变量接收返回信息

$response = Invoke-WebRequest -Uri "https://www.example.com"
$htmlcontent = $response.Content
$htmlcontent