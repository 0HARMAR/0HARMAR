clear; clc; close all;

% 读取数据，根据is_qian_bei的值选择不同的函数
is_qian_bei = 0;
ok = 1;
if is_qian_bei == 1
    [data1, name1] = read_qian_bei(ok); % 读取qian_bei数据
else
    [data1, name1] = read_gao_jia(ok);  % 读取gao_jia数据
end

% 数据处理（注释掉的数据检查和调整）
% for i = 1:size(data1, 1)
%     if sum(data1(i, :)) ~= 100
%         data1(i, :) = data1(i, :) / sum(data1(i, :)) * 100;
%     end
% end

% 计算距离矩阵并进行层次聚类分析
D = pdist(data1, 'minkowski', 2);
Z = linkage(D, 'ward');

% 绘制树状图
H = dendrogram(Z, 'labels', name1);
set(H, 'color', 'k', 'linewidth', 1.3);

% 设置标题，根据is_qian_bei的值选择不同的标题
if is_qian_bei == 1
    title('3#&,.5?7', 'FontSize', 16);
else
    title('(+&,.5?7', 'FontSize', 16);
end

% 设置坐标轴标签
xlabel('*:$', 'FontSize', 12);
ylabel('Scale', 'FontSize', 12);

% 聚类分析，分成2类
k = 2;
T = cluster(Z, k);

% 输出每个聚类的成员
for i = 1:k
    tm = find(T == i); % 找到第i类的成员
    tm = tm'; % 转置为行向量
    fprintf(2, '&%d.&<x\n', i); % 输出类编号
    for j = 1:length(tm)
        fprintf("%s ", name1{tm(j)}); % 输出成员名称
    end
    fprintf("\n");
end
