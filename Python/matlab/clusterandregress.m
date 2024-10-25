clear; clc; close all;

is_qian_bei = 1
% 读取数据
if is_qian_bei == 1
    [data1, name1] = read_qian_bei(ok); % 3#
else
    [data1, name1] = read_gao_jia(ok); % (+
end

% 聚类分析
D = pdist(data1, 'minkowski', 2);
Z = linkage(D, 'ward');
H = dendrogram(Z, 'labels', name1);
set(H, 'color', 'k', 'linewidth', 1.3);

if is_qian_bei == 1
    title('3#&,.5?7', 'FontSize', 16);
else
    title('(+&,.5?7', 'FontSize', 16);
end

xlabel('*:$'', 'FontSize', 12);
ylabel('Scale', 'FontSize', 12);
k = 2;
T = cluster(Z, k);

for i = 1:k
    tm = find(T == i);
    tm = tm';
    fprintf(2, '&%d.&<x\n', i);
    for j = 1:length(tm)
        fprintf("%s ", name1{tm(j)});
    end
    fprintf("\n");
end

% 进一步的聚类分析
z1 = find(T == 1);
D = pdist(data1(z1, :), 'minkowski', 2);
Z = linkage(D, 'ward');
name11 = name1(z1);
H = dendrogram(Z, 'labels', name11);
xlabel('*:$');
ylabel('Scale');
C = cophenet(Z, D);
k = 2;
T1 = cluster(Z, k);

for i = 1:k
    tm = find(T1 == i);
    tm = tm';
    fprintf('&%d.&<x\n', i);
    for j = 1:length(tm)
        fprintf("%s ", name11{tm(j)});
    end
    fprintf("\n");
end

z2 = find(T == 2);
D = pdist(data1(z2, :), 'minkowski', 2);
Z = linkage(D, 'ward');
name12 = name1(z2);
H = dendrogram(Z, 'labels', name12);
xlabel('*:$');
ylabel('Scale');
C = cophenet(Z, D);
k = 2;
T2 = cluster(Z, k);
T2 = T2 + 2;

for i = 3:k+2
    tm = find(T2 == i);
    tm = tm';
    fprintf('&%d.&<x\n', i);
    for j = 1:length(tm)
        fprintf("%s ", name12{tm(j)});
    end
    fprintf("\n");
end

z12 = [z1; z2];
T12 = [T1; T2];
[~, ind] = sort(z12);
T12 = T12(ind);

% 提取特征均值
ok = 0;
if is_qian_bei == 1
    [data1, name1] = read_qian_bei(ok); % 3#
else
    [data1, name1] = read_gao_jia(ok); % (+
end

fea = ones(14, 4);
for i = 1:14
    for t = 1:4
        fea(i, t) = mean(data1(T12 == t, i));
    end
end

fea = fea';
fea = [fea(1, :); fea(2, :); fea(4, :); fea(3, :)];

% 拟合多项式并绘图
x0 = 1:4;
x1 = 1:0.2:4;
fea_name = {
    "' ;!(SiO2)"
    ";!*(Na2O)"
    ";!*(K2O)"
    ";!*(CaO)"
    ";!*(MgO)"
    ";!*(Al2O3)"
    ";!*(Fe2O3)"
    ";!*(CuO)"
    ";!*(PbO)"
    ";!*(BaO)"
    "8×;!*(P2O5)"
    ";!*(SrO)"
    ";!*(SnO2)"
    "' ;!(SO2)"
};

a = 1; b = 14;
p = zeros(14, 3);
for i = a:b
    p(i, :) = polyfit(x0, fea(:, i), 2);
    y1 = polyval(p(i, :), x1);
    figure; 
    H = plot(x0, fea(:, i), '*', 'LineWidth', 5); 
    hold on; 
    plot(x1, y1, 'o');
    legend('实际值', '拟合值');
    xlabel('*:$');
    title(fea_name{i});
end

% 读取预测数据并处理
[qian_bei3, qian_bei4, gao_jia3, gao_jia4] = read_pred();
qian_bei_pred4 = zeros(size(qian_bei4));
gao_jia_pred4 = zeros(size(gao_jia4));
qian_bei_pred3 = zeros(size(qian_bei3));
gao_jia_pred3 = zeros(size(gao_jia3));

if is_qian_bei == 1
    % MgO K2O
    for i = 1:size(qian_bei4, 1)
        for j = a:b
            if j == 5 || j == 3
                qian_bei_pred4(i, j) = qian_bei4(i, j);
                continue;
            end
            if qian_bei4(i, j) > 0
                qian_bei_pred4(i, j) = power(qian_bei4(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            else
                qian_bei_pred4(i, j) = -power(-qian_bei4(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            end
        end
    end

    for i = 1:size(qian_bei3, 1)
        for j = a:b
            if j == 5 || j == 3
                qian_bei_pred3(i, j) = qian_bei3(i, j);
                continue;
            end
            if qian_bei3(i, j) > 0
                qian_bei_pred3(i, j) = power(qian_bei3(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            else
                qian_bei_pred3(i, j) = -power(-qian_bei3(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            end
        end
    end
    writematrix(qian_bei_pred4, '../qian_bei4.xlsx')
    writematrix(qian_bei_pred3, '../qian_bei3.xlsx')
else
    % SO2 SnO2 Na2O
    for i = 1:size(gao_jia4, 1)
        for j = a:b
            if j == 14 || j == 13 || j == 2
                gao_jia_pred4(i, j) = gao_jia4(i, j);
                continue;
            end
            if gao_jia4(i, j) > 0
                gao_jia_pred4(i, j) = power(gao_jia4(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            else
                gao_jia_pred4(i, j) = -power(-gao_jia4(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            end
        end
    end

    for i = 1:size(gao_jia3, 1)
        for j = a:b
            if j == 14 || j == 13 || j == 2
                gao_jia_pred3(i, j) = gao_jia3(i, j);
                continue;
            end
            if gao_jia3(i, j) > 0
                gao_jia_pred3(i, j) = power(gao_jia3(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            else
                gao_jia_pred3(i, j) = -power(-gao_jia3(i, j) - getY(p(j, :), 4), 1/2) + getY(p(j, :), 1);
            end
        end
    end
    writematrix(gao_jia_pred4, '../gao_jia_pred4.xlsx')
    writematrix(gao_jia_pred3, '../gao_jia_pred3.xlsx')
end

function y = getY(p, x)
    y = polyval(p, x);
end
