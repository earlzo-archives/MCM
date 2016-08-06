% 数据输入
clear
load D:\Projects\PyCharm\math_modeling_learning\digits_dataset\didits.mat

%设置固定的随机种子保证每次初始状态一致，不是必须
setdemorandstream(391418381)

% 参数：隐含层神经元数，训练方法，性能评估方法
% 默认训练方法：量化共轭梯度法
% 默认：性能评估方法
net = patternnet(10, 'trainscg', 'crossentropy');

%训练网络
net = train(net,training_data_sample,training_data_target);

% 查看网络
% view(net)
y = net(test_data_sample);

% 评估结果
perf = perform(net,test_data_target,y);
classes = vec2ind(y);
