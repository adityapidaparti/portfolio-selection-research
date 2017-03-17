% projection to simplex
function [new_v] = find_y(v,z)
  % fprintf('=== In find_y ===');
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
