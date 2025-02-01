{
        "type": "cppbuild",
        "label": "C/C++: clang++.exe build active file",
        "command": "C:\\Users\\hemingyang\\Downloads\\clang+llvm-18.1.8-x86_64-pc-windows-msvc\\bin\\clang++.exe",
        "args": [
            "-fcolor-diagnostics",
            "-g",
            "${file}",
            "-o",
            "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "-L\"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\ATLMFC\\lib\\x64\"",
        "-L\"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\lib\\x64\"",
        "-L\"C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.22621.0\\ucrt\\x64\"",
        "-L\"C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.22621.0\\um\\x64\"",
        "-L\"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\ATLMFC\\lib\\x86\"",
        "-L\"C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\lib\\x86\"",
        "-L\"C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.22621.0\\ucrt\\x86\"",
        "-L\"C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.22621.0\\um\\x86\""
        ],
        "options": {
            "cwd": "C:\\Users\\hemingyang\\Downloads\\clang+llvm-18.1.8-x86_64-pc-windows-msvc\\bin",
            "shell": {
                "executable": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
                "args": [
                    "-NoLogo",
                    "-NoProfile"
                ]
            }
        },
        "problemMatcher": [
            "$gcc"
        ],
        "group": {
            "kind": "build",
            "isDefault": true
        },
        "detail": "Task generated for clang++."
    },

    {
    "name": "(lldb) Launch", // 使用 LLDB 调试
    "type": "lldb-dap",
    "request": "launch",
    "program": "${workspaceFolder}/${fileBasenameNoExtension}.exe", // 指向生成的同名可执行文件
    "args": [],
    "stopAtEntry": false,
    "cwd": "${fileDirname}",
    "environment": [],
    "externalConsole": false,
    "MIMode": "lldb", // 设置调试器模式为 LLDB
    "miDebuggerPath": "c:\\Users\\hemingyang\\Downloads\\clang+llvm-18.1.8-x86_64-pc-windows-msvc\\bin\\lldb.exe", // LLDB 的路径
    "setupCommands": [
        {
            "description": "Enable pretty-printing for lldb",
            "text": "-enable-pretty-printing",
            "ignoreFailures": true
        }
    ]
}

 {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/C++/**",
                "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\include",
                "C:\\Users\\hemingyang\\Downloads\\clang+llvm-18.1.8-x86_64-pc-windows-msvc\\lib\\clang\\18\\include",
                "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.40.33807\\ATLMFC\\include",
                "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Auxiliary\\VS\\include",
                "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\ucrt",
                "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\um",
                "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\shared",
                "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\winrt",
                "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.22621.0\\cppwinrt",
                "C:\\Program Files\\Java\\jdk-21\\include\\win32",
                "${workspaceFolder}/Java/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "compilerPath": "C:\\Users\\hemingyang\\Downloads\\clang+llvm-18.1.8-x86_64-pc-windows-msvc\\bin\\clang++.exe",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }