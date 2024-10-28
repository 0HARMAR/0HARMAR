在settings.json文件里添加
"terminal.integrated.profiles.windows": {
    "PowerShell": {
        "source": "PowerShell",
        "args": ["-NoExit", "-Command", "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8"]
    }
},
每次powershell启动会将编码设置为utf-8