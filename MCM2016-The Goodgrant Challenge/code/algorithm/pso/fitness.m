function y = fitness(x)
% x Ϊ����ҪͶ��ѧУ�ı���
% r Ϊ��ӦѧУ��������
load('');
y = 1/sum(r*x);
end

