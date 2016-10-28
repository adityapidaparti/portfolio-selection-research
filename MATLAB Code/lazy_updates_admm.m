%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Authors: Nicholas Johnson and Puja Das (University of Minnesota)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
dataset = 'nyse';
results_path = strcat('../results/', dataset, '/');
dataset_path = '../datasets/';

load(dataset);
x = data'; % price relative matrix

gamma = 0.0; % Transaction cost
rho = 0.1; % Augmentation term
beta = 2; % Weight on L2 norm
[num_stock num_days] = size(x);

for eta = [1e-6 1e-5 1e-4 1e-3 1e-2 0.1 1 10 100] % Weight on log
  for alpha = [1e-6 1e-5 1e-4 1e-3 1e-2 0.1 1 10 100] % Weight on L1 norm (bigger alpha aka trade less frequently)

    fprintf('** eta = %d, alpha = %f, gamma = %f, rho = %f, beta = %f **\n', eta, alpha, gamma, rho, beta);

    % Init variables
    weight = zeros(num_stock, num_days);
    wealth = zeros(num_days, 1);
    wealth(1,1) = 1; % Start with 1 dollar

    % Portfolio for the first day
    weight(:, 1) = ones(num_stock,1) * (1/num_stock);

    for t = 2:3
      fprintf('Day: %d, Wealth: %d \n', t, wealth(t-1) );

      % ADMM
      w = sparse_port_admm(weight(:,t-1), x(:,t-1), eta, beta, alpha, rho);

      weight(:,t) = w;
      wealth(t,1) = wealth(t-1,1)*(weight(:,t)'*x(:,t))-gamma*abs(wealth(t-1,1))*norm(weight(:,t-1)-weight(:,t),1);
    end
  end % end alpha
end % end eta
