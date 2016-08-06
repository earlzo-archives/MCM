clear ;
close all;

ri = [0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.51];
load AHP_matrix.mat

results = cell(1,3);

matrix = {m1, m2, m3};

for i = 1:3
m=matrix{1, i};
display(m);
[~, n] = size(m);
[x, y] = eig(m);
eigenvalue = diag(y);
lambda = eigenvalue(1);
cil = (lambda - n)/(n-1);
crl = cil/ri(n);
w = x(:,1)/sum(x(:,1));

r = struct;
r.lambda = lambda;
r.w = w;
r.cil = cil; 
r.crl = crl;
results{1, i} = r;
i = i + 1;
end

save AHP_results.mat results
