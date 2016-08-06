%http://cn.mathworks.com/help/releases/R2015a/gads/particleswarm.html
% ���Ż����� ����Ӧ�Ⱥ���������Ϊ����
fun = @fitness;
% ������ ������������Ԫ�ظ���
nvars = 2;
% �ٶ� vmax = min(ub-lb, options.InitialSwarmSpan);
% �����½�
lb = [-50;-50];
% �����Ͻ�
ub = -lb;
%ѡ��
options = optimoptions('particleswarm');

%options.SelfAdjustment %�����������  default 1.49
%options.SocialAdjustment %Ⱥ���������  default 1.49
%options.InertiaRange %���Է�Χ

%options.SwarmSize %��Ⱥ��С  Default is min(100,10*nvars)
%options.MaxIter %����������
%options.MaxTime %���ִ��ʱ��

%options.CreationFcn %��Ⱥ��ʼ��������û����ʹ��Ĭ��
%options.InitialSwarm %�Լ���ʼ������Ⱥ

%options.InitialSwarmSpan %@pswcreationuniform ��������Ⱥ��Χ
%options.MinFractionNeighbors %Minimum adaptive neighborhood size, a scalar from 0 to 1. Default is 0.25. 

options.HybridFcn = @fmincon; %��Ϻ������������㷨����Ա�

% �㷨�޹ز���
%options.ObjectiveLimit  %��С�����С

% options.OutputFcns  %�����㷨��������
options.PlotFcns = @pswplotfitness; %��������

options.Display = 'iter';  %����̨��ʾ��Ϣ��ʽ
% options.DisplayInterval %����̨��ʾ��Ϣ����
% options.FunValCheck %��麯������Ƿ�Ϸ�

%options.StallIterLimit 
% options.StallTimeLimit  
% options.TolFun 

% options.UseParallel 
% options.Vectorized

%Control random number generation
rng default % For reproducibility

[x,fval,exitflag] = particleswarm(fun,nvars,lb,ub,options);
