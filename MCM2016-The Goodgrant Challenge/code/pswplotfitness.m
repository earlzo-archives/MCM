function stop = pswplotfitness(optimValues,state)
% optimValues Structure
% funccount	�ܼƺ���ִ�д���
% bestx	����ֵ�Ա���
% bestfval	����ֵ�����
% iteration	��������
% meanfval	��ǰ��������ƽ��ֵ
% stalliterations	�ܴ��ϴ�����ֵ�ı�����Ĵ���
% swarm	����λ�þ���
% swarmfvals ����ֵ����

%��������Ⱥ�㷨ȫ������ֵ����������ı仯
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
