function [x,fval,exitflag] = pso(I, q, e)
% function [x,fval,exitflag] = pso(I)
display(size(I))

% 适应度函数
function r = fitness(w)
% w 为所有要投的学校的比例
% r 为对应学校的收益率
w = w/sum(w);
% 小于风险因子
qw = q .* w;

flag = all(  qw  < e);
if  flag == 1
    r = -sum(I .* w);
else
    fprintf( '----最大值: %f	最小值: %f----\n', max(qw), min(qw));
    r = inf;
end

end


%http://cn.mathworks.com/help/releases/R2015a/gads/particleswarm.html
% 待优化函数 即适应度函数，参数为个体
fun = @fitness;
% 变量数 即个体向量的元素个数
s = size(I);
nvars = s(2);
% 速度 vmax = min(ub-lb, options.InitialSwarmSpan);
% 搜索下界
lb = zeros(1, nvars);
% 搜索上界
ub = 0.5 * ones(1, nvars);
%选项
options = optimoptions('particleswarm');

%options.SelfAdjustment %个体加速因子  default 1.49
%options.SocialAdjustment %群体加速因子  default 1.49
options.InertiaRange = [0.8, 1.1];%惯性范围, 默认[0.1, 1.1]

%options.SwarmSize %种群大小  Default is min(100,10*nvars)
%options.MaxIter %最大迭代次数
options.MaxTime = 60 * 2; %最大执行时间

%options.CreationFcn %种群初始化函数，没有则使用默认
%options.InitialSwarm %自己初始化的种群

%options.InitialSwarmSpan %@pswcreationuniform 创建的种群范围
%options.MinFractionNeighbors %Minimum adaptive neighborhood size, a scalar from 0 to 1. Default is 0.25. 

% options.HybridFcn = @fmincon; %混合函数，用来与算法结果对比

% 算法无关参数
%options.ObjectiveLimit  %最小对象大小

% options.OutputFcns  %处理算法迭代过程
% options.PlotFcns = @pswplotaranges; %与上类似

options.Display = 'iter';  %控制台显示信息方式
options.DisplayInterval = 50; %控制台显示信息周期
% options.FunValCheck %检查函数输出是否合法

% 如果不改善最有名的目标函数值的最大次数， 默认20。
options.StallIterLimit = 100;
% 如果不改善最有名的目标函数值的最大秒数。
% options.StallTimeLimit  
% Nonnegative scalar with default 1e-6. Iterations end when the relative change in best objective function value over the last StallIterLimit iterations is less than options.TolFun.
% options.TolFun 

% options.UseParallel 
% options.Vectorized

%Control random number generation
% rng default % For reproducibility

[x,fval,exitflag] = particleswarm(fun,nvars,lb,ub,options);
end
