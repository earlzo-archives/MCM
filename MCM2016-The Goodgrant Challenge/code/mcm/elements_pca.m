function [lambda, vec2, stf, ind] = elements_pca(elements_file)
data = load(elements_file);
display(size(data.X))
% ���ݱ�׼��
normal_X = zscore(data.X);
r=corrcoef(normal_X);  %�������ϵ������
%�����������ϵ������������ɷַ�����x����Ϊr�����������������ɷֵ�ϵ��
[x,y,z]=pcacov(r); %yΪr������ֵ��zΪ�������ɷֵĹ�����
f=repmat(sign(sum(x)),size(x,1),1); %������xͬά����Ԫ��Ϊ��1�ľ���
x=x.*f; %�޸����������������ţ�ÿ�����������������з����͵ķ��ź���ֵ
num=3;  %numΪѡȡ�����ɷֵĸ���
df=normal_X*x(:,[1:num]);  %����������ɷֵĵ÷�
tf=df*z(1:num)/100; %�����ۺϵ÷�
[stf,ind]=sort(tf,'descend');  %�ѵ÷ְ��մӸߵ��͵Ĵ�������
stf=stf';
ind=ind';

display()
end
