%http://cn.mathworks.com/help/releases/R2015a/gads/particleswarm.html
% 待优化函数 即适应度函数，参数为个体
fun = @fitness;
% 变量数 即个体向量的元素个数
nvars = 2;
% 速度 vmax = min(ub-lb, options.InitialSwarmSpan);
% 搜索下界
lb = [-50;-50];
% 搜索上界
ub = -lb;
%选项
options = optimoptions('particleswarm');

%options.SelfAdjustment %个体加速因子  default 1.49
%options.SocialAdjustment %群体加速因子  default 1.49
%options.InertiaRange %惯性范围

%options.SwarmSize %种群大小  Default is min(100,10*nvars)
%options.MaxIter %最大迭代次数
%options.MaxTime %最大执行时间

%options.CreationFcn %种群初始化函数，没有则使用默认
%options.InitialSwarm %自己初始化的种群

%options.InitialSwarmSpan %@pswcreationuniform 创建的种群范围
%options.MinFractionNeighbors %Minimum adaptive neighborhood size, a scalar from 0 to 1. Default is 0.25. 

options.HybridFcn = @fmincon; %混合函数，用来与算法结果对比

% 算法无关参数
%options.ObjectiveLimit  %最小对象大小

% options.OutputFcns  %处理算法迭代过程
options.PlotFcns = @pswplotfitness; %与上类似

options.Display = 'iter';  %控制台显示信息方式
% options.DisplayInterval %控制台显示信息周期
% options.FunValCheck %检查函数输出是否合法

%options.StallIterLimit 
% options.StallTimeLimit  
% options.TolFun 

% options.UseParallel 
% options.Vectorized

%Control random number generation
rng default % For reproducibility

[x,fval,exitflag] = particleswarm(fun,nvars,lb,ub,options);
