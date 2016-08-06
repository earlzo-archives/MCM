I_path = 'mat/I.mat';
q_path = 'mat/q.mat';
load(I_path);
load(q_path);

[x,fval,exitflag] = pso(I, q, 0.0005);
x = x/sum(x);
display(max(x));
display(min(x));
display(fval);
plot(x);
