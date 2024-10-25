clc; close all; clear all; warning off; % 清除变量
rand('seed', 100);
randn('seed', 100);
format long g;

% 材料和数据
materials = {'棉花', '羽绒', '聚酯纤维', '聚丙烯纤维', '聚酰胺纤维', '再生纤维'};
data = [
    0.045, 0.117, 0.04, 0.2, 0.3, 0.045;  % 热导率
    0.65, 0.25, 0.15, 0.25, 0.026, 0.55;  % 热阻值
    0.04, 0.025, 0.03, 0.2, 0.2, 0.04;    % 总热导传系数
    0.4, 1.125, 0.5, 0.4, 0.5, 0.6;       % CLO值
    0.15, 2, 1.8, 1.6, 0.4, 0.4;          % 纤维厚度 (cm)
    0.25, 0.1, 1.38, 0.9, 1.15, 1.5       % 纤维密度
];

% 转置数据矩阵
data = data';

% 属性的权重，可以根据实际情况调整
weights = [0.2, 0.3, 0.2, 0.1, 0.1, 0.1];

% 数据标准化
normalized_data = bsxfun(@rdivide, data, sqrt(sum(data.^2, 1)));

% 加权标准化数据
weighted_data = bsxfun(@times, normalized_data, weights);

% 确定正理想解和负理想解
ideal_solution = max(weighted_data, [], 1);
negative_ideal_solution = min(weighted_data, [], 1);

% 计算各方案到正理想解和负理想解的距离
distances_to_ideal = sqrt(sum(bsxfun(@minus, weighted_data, ideal_solution).^2, 2));
distances_to_negative_ideal = sqrt(sum(bsxfun(@minus, weighted_data, negative_ideal_solution).^2, 2));

% 计算各方案的接近度
closeness = distances_to_negative_ideal ./ (distances_to_ideal + distances_to_negative_ideal);

% 对接近度进行排序，得到方案的排序结果
[sorted_closeness, sorted_indices] = sort(closeness, 'descend');
disp('材料的排序结果为：');
disp(materials(sorted_indices));

% 数据可视化
figure;
bar(closeness, 'FaceColor', 'b');
title('TOPSIS评价结果');
xlabel('材料');
ylabel('接近度');
set(gca, 'xticklabel', materials);
ylim([0 1.1]);
grid on;
