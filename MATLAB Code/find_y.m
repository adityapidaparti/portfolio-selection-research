% projection to simplex
function [new_v] = find_y(v,z)
  mu = sort(v,'descend');
  for j =1:length(mu)
    residual = mu(j) - ((sum(mu(1:j))-z)/j);
    % fprintf('residual: %f\n', residual);
    if(residual >0)
      rho = j;
    end
  end

  theta = (sum(mu(1:rho))-z)/rho;
  % fprintf('rho %f\n', rho)
  % fprintf('sum: %fs\n',  sum(mu(1:rho)));

  new_v = max((v-theta),0);

end
