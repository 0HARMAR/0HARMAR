```bash
cd "你的项目路径"      # 进入你的项目文件夹
git init               # 初始化 Git 仓库（如果还没有初始化）
git add .              # 将所有文件添加到暂存区
git commit -m "Initial commit"  # 提交文件并附上提交信息
```

### 连接到 GitHub 并上传代码
```bash
git remote add origin https://github.com/your-username/your-repository.git
```

### 推送到 GitHub
```bash
git push -u origin main
```

### 设置忽略文件的方法
1. 创建一个 `.gitignore` 文件，在文件里放想要忽略的文件。
2. 清除暂存区的文件，保持文件在工作区：
   ```bash
   git rm -r --cached .
   ```

### 设置自动行尾处理
```bash
git config --global core.autocrlf true
```

### 初始化后，基本的步骤是
```bash
git add 
git commit
git push
```
