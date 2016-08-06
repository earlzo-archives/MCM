function [x,fval,exitflag] = pso(I, q, e)
% function [x,fval,exitflag] = pso(I)
display(size(I))

% ��Ӧ�Ⱥ���
function r = fitness(w)
% w Ϊ����ҪͶ��ѧУ�ı���
% r Ϊ��ӦѧУ��������
w = w/sum(w);
% С�ڷ�������
qw = q .* w;

flag = all(  qw  < e);
if  flag == 1
    r = -sum(I .* w);
else
    fprintf( '----���ֵ: %f	��Сֵ: %f----\n', max(qw), min(qw));
    r = inf;
end

end


%http://cn.mathworks.com/help/releases/R2015a/gads/particleswarm.html
% ���Ż����� ����Ӧ�Ⱥ���������Ϊ����
fun = @fitness;
% ������ ������������Ԫ�ظ���
s = size(I);
nvars = s(2);
% �ٶ� vmax = min(ub-lb, options.InitialSwarmSpan);
% �����½�
lb = zeros(1, nvars);
% �����Ͻ�
ub = 0.5 * ones(1, nvars);
%ѡ��
options = optimoptions('particleswarm');

%options.SelfAdjustment %�����������  default 1.49
%options.SocialAdjustment %Ⱥ���������  default 1.49
options.InertiaRange = [0.8, 1.1];%���Է�Χ, Ĭ��[0.1, 1.1]

%options.SwarmSize %��Ⱥ��С  Default is min(100,10*nvars)
%options.MaxIter %����������
options.MaxTime = 60 * 2; %���ִ��ʱ��

%options.CreationFcn %��Ⱥ��ʼ��������û����ʹ��Ĭ��
%options.InitialSwarm %�Լ���ʼ������Ⱥ

%options.InitialSwarmSpan %@pswcreationuniform ��������Ⱥ��Χ
%options.MinFractionNeighbors %Minimum adaptive neighborhood size, a scalar from 0 to 1. Default is 0.25. 

% options.HybridFcn = @fmincon; %��Ϻ������������㷨����Ա�

% �㷨�޹ز���
%options.ObjectiveLimit  %��С�����С

% options.OutputFcns  %�����㷨��������
% options.PlotFcns = @pswplotaranges; %��������

options.Display = 'iter';  %����̨��ʾ��Ϣ��ʽ
options.DisplayInterval = 50; %����̨��ʾ��Ϣ����
% options.FunValCheck %��麯������Ƿ�Ϸ�

% �����������������Ŀ�꺯��ֵ���������� Ĭ��20��
options.StallIterLimit = 100;
% �����������������Ŀ�꺯��ֵ�����������
% options.StallTimeLimit  
% Nonnegative scalar with default 1e-6. Iterations end when the relative change in best objective function value over the last StallIterLimit iterations is less than options.TolFun.
% options.TolFun 

% options.UseParallel 
% options.Vectorized

%Control random number generation
% rng default % For reproducibility

[x,fval,exitflag] = particleswarm(fun,nvars,lb,ub,options);
end
