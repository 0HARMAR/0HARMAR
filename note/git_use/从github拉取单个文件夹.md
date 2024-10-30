启动稀疏检测模式
git config core.sparseCheckout true

向.git/info/sparse-checkout文件中添加要拉取的文件
默认路径是github上项目的根路径
例如 note/*表示拉取note文件夹下所有文件，包括子文件夹

拉取
git pull