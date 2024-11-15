# 添加路径到path系统变量
$first_arg = $args[0]

Write-Host "第一个参数是 $first_arg"

# 获取源环境变量
$currentSystemPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)

# 更新后的环境变量
$updatedPath = $currentSystemPath + ";" + $first_arg

# 添加到系统环境变量
[System.Environment]::SetEnvironmentVariable("PATH", $updatedPath, [System.EnvironmentVariableTarget]::Machine)