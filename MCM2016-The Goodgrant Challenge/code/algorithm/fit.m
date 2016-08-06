clear ;
close all;
load('D:\Projects\PyCharm\math_modeling_learning\TN-TP-NP.mat')

setdemorandstream(491218382)

% best_perf = [];
% best_vperf = [];
% best_tperf = [];

for i = 1:25
net = fitnet(i);

[net,tr] = train(net,x,t);
% nntraintoo
% view(net);

best_perf(i) = tr.best_perf;
best_vperf(i) = tr.best_vperf;
best_tperf(i) = tr.best_tperf;

plotperform(tr)

% testX = x(:,tr.testInd);
% testT = t(:,tr.testInd);
% testY = net(testX);
% perf = mse(net,testT,testY);

% y = net(x);
% plotregression(t,y, 'Regression');
end

[best, best_idx] = min(best_perf);
plot(1:25,best_perf, '-',best_idx  , best, 'o');
xlabel('Number of Neurons');
ylabel('Best Performance');
trainlm
