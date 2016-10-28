%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Inputs: w_t   - portfolio for the previous day
%         x_t   - price relative for the previous day
%         eta   - weight on the log term
%         beta  - weight on the l-2 term
%         gamma - weight on the l-1 term
%         rho   - weight on the augmented lagrangian
% Outputs: w -  portfolio for the next day or w_t+1
%
% Authors: Nicholas Johnson and Puja Das (University of Minnesota)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [w] = sparse_port_admm(w_t, x_t, eta, beta, gamma, rho)
  % Input


  QUIET    = 1;
  MAX_ITER = 1000;
  ABSTOL   = 1e-4;
  RELTOL   = 1e-2;
  n = length(w_t);
  w = zeros(n,1);
  z = zeros(n,1);
  u = zeros(n,1);
  const = w_t'*x_t; %equal to sum of each weight multiplied by its price relative

  %debugging
  count = 0;

  for k=1:MAX_ITER %iterating through 3 sub-problems until convergence or max iterations
    %     W-update (portfolio update)
    w_temp = (eta/((rho+beta)*const))*x_t + w_t + (rho/(rho+beta))*z - (rho/(rho+beta))*u; %Inside of 1st step Algorithm 1
    [w] = find_y(w_temp,1); %projects onto a probability distribution of size 1

    %     Z-update
    %Step right below portfolio update
    %Very similar to above
    zold = z;
    thresh = gamma/rho;
    z_temp = (w - w_t + u);

    z = shrinkage(z_temp,thresh);
    count = count + 1;
    if count == 10
      fprintf('z: %f\n', z);
      throw(MException('a', 'b'));
    end


    %     U-update
    %Last step; below above
    u = u + (w - w_t - z);

    % Compute primal and dual residual
    %The convergence/stopping criteria
    history.r_norm(k)  = norm(w - w_t - z);
    history.s_norm(k)  = norm(-rho*(z - zold));

    history.eps_pri(k) = sqrt(n)*ABSTOL + RELTOL*max([norm(w),norm(-w_t), norm(-z)]);
    history.eps_dual(k)= sqrt(n)*ABSTOL + RELTOL*norm(rho*u);

    if ~QUIET
      fprintf('%3d\t%10.4f\t%10.4f\t%10.4f\t%10.4f\n', k, ...
        history.r_norm(k), history.eps_pri(k), ...
        history.s_norm(k), history.eps_dual(k));
    end

    % Stopping Criterion (close enough to optimum solution)
    if (history.r_norm(k) < history.eps_pri(k) && ...
        history.s_norm(k) < history.eps_dual(k))
      break;
    end
  end % end k iteration
end % end function

% projection to simplex
function [new_v] = project_simplex(v,z)
  mu = sort(v,'descend');
  for j =1:length(mu)
    residual = mu(j) - ((sum(mu(1:j))-z)/j);
    if(residual >0)
      rho = j;
    end
  end
  theta = (sum(mu(1:rho))-z)/rho;
  new_v = max((v-theta),0);
end

% Soft Thresholding
function z = shrinkage(x, kappa)
  % fprintf('\n x is %f', x);
  % fprintf(' kappa is %f \n', kappa);

  z = max( 0, x - kappa ) - max( 0, -x - kappa );
  fprintf('\nshrinkage z: %f', z);
end
