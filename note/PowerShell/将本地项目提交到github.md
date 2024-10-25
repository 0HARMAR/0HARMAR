cd "你的项目路径"      # 进入你的项目文件夹
git init               # 初始化 Git 仓库（如果还没有初始化）
git add .              # 将所有文件添加到暂存区
git commit -m "Initial commit"  # 提交文件并附上提交信息

连接到github并上传代码
git remote add origin https://github.com/your-username/your-repository.git

推送到github
git push -u origin master

设置忽略文件的方法
创建一个.gitignore文件，在文件里放想要忽略的文件

git rm -r --cached .       # 清除暂存区的文件，保持文件在工作区