function y = fitness(x)
% x 为所有要投的学校的比例
% r 为对应学校的收益率
load('');
y = 1/sum(r*x);
end

