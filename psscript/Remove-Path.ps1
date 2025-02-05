param(
    [Parameter(Mandatory=$true, HelpMessage="要删除的路径")]
    [string]$PathToRemove,
    
    [Parameter(HelpMessage="作用域（User/Machine/Both）")]
    [ValidateSet('User', 'Machine', 'Both')]
    [string]$Scope = 'User'
)

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# 确定要处理的作用域
$scopesToProcess = switch ($Scope) {
    'User'      { 'User' }
    'Machine'   { 'Machine' }
    'Both'      { 'User', 'Machine' }
}

foreach ($scope in $scopesToProcess) {
    # 检查Machine作用域权限
    if ($scope -eq 'Machine' -and -not $isAdmin) {
        Write-Error "修改系统环境变量需要管理员权限，请以管理员身份运行此脚本。"
        continue
    }

    # 获取当前作用域的PATH
    $currentPath = [Environment]::GetEnvironmentVariable('Path', $scope)
    if ([string]::IsNullOrEmpty($currentPath)) {
        Write-Warning "[$scope] PATH为空，跳过处理。"
        continue
    }

    # 标准化要删除的路径（忽略大小写和结尾反斜杠）
    $normalizedRemove = $PathToRemove.Trim().TrimEnd('\').ToLower()

    # 分割并过滤路径
    $newPaths = $currentPath -split ';' | Where-Object {
        $_.Trim() -ne '' -and 
        $_.Trim().TrimEnd('\').ToLower() -ne $normalizedRemove
    }

    # 重新组合路径
    $newPath = $newPaths -join ';'

    # 更新环境变量
    [Environment]::SetEnvironmentVariable('Path', $newPath, $scope)
    Write-Host "[$scope] 已删除路径: $PathToRemove"
}

Write-Host "操作完成！部分变更可能需要重启或重新打开终端才能生效。"