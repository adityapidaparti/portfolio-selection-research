% projection to simplex
function [new_v] = find_y(v,z)
  % fprintf('=== In find_y ===');
  mu = sort(v,'descend');
  for j =1:length(mu)
    residual = mu(j) - ((sum(mu(1:j))-z)/j);
    % fprintf('residual: %f\n', residual);
    if(residual >0)
      rho = j;
      % fprintf('rho: %f\n', rho)
    end
  end
  theta = (sum(mu(1:rho))-z)/rho;
  % fprintf('rho %f\n', rho)
  % fprintf('sum: %fs\n',  sum(mu(1:rho)));

  % fprintf('\nmu dist: ')
  % mu(1:rho)
  % fprintf('\nrho: %f', rho);
  % fprintf('\nz: %f', z);
  new_v = max((v-theta),0);
  % fprintf('\n=== End find_y\n');

end
