% ��������
clear
load D:\Projects\PyCharm\math_modeling_learning\digits_dataset\didits.mat

%���ù̶���������ӱ�֤ÿ�γ�ʼ״̬һ�£����Ǳ���
setdemorandstream(391418381)

% ��������������Ԫ����ѵ��������������������
% Ĭ��ѵ�����������������ݶȷ�
% Ĭ�ϣ�������������
net = patternnet(10, 'trainscg', 'crossentropy');

%ѵ������
net = train(net,training_data_sample,training_data_target);

% �鿴����
% view(net)
y = net(test_data_sample);

% �������
perf = perform(net,test_data_target,y);
classes = vec2ind(y);
