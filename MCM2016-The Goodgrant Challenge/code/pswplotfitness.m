function stop = pswplotfitness(optimValues,state)
% optimValues Structure
% funccount	总计函数执行次数
% bestx	最优值自变量
% bestfval	最优值因变量
% iteration	迭代次数
% meanfval	当前迭代函数平均值
% stalliterations	总从上次最优值改变迭代的次数
% swarm	粒子位置矩阵
% swarmfvals 函数值矩阵

%绘制粒子群算法全局最优值随迭代次数的变化
stop = false; % This function does not stop the solver
switch state
    case 'init'
        subplot(1,1,1)
        title('FunVal changes with iteration');
        xlabel('Iteration','interp','none'); % Iteration number at the bottom
        ylabel('Fitness');
        tag = 'psoplotfitness';
        plot(optimValues.bestfval, 'Tag',tag);
        setappdata(gcf,'t0',tic); % Set up a timer to plot only when needed
    case 'iter'
            tag = 'psoplotfitness';
            plotHandle = findobj(get(gca,'Children'),'Tag',tag); % Get the subplot
            xdata = plotHandle.XData; % Get the X data from the plot
            newX = [xdata optimValues.iteration]; % Add the new iteration
            plotHandle.XData = newX; % Put the X data into the plot
            ydata = plotHandle.YData; % Get the Y data from the plot
            newY = [ydata optimValues.bestfval]; % Add the new value
            plotHandle.YData = newY; % Put the Y data into the plot
        if toc(getappdata(gcf,'t0')) > 1/30 % If 1/30 s has passed
          drawnow % Show the plot
          setappdata(gcf,'t0',tic); % Reset the timer
        end
    case 'done'
        % No cleanup necessary
end
