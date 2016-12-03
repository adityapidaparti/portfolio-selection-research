%EG algorithm
%M is the relative price matrix
%eta is the learning rate
%weight is the protfolio
function [Weight, wealth] = eg_Portfolio(M, eta)

[num_days num_stock] = size(M);

Weight = zeros(num_days, num_stock);
wealth = zeros(num_days, 1);
wealth(1,1) = 1; % Start with 1 dollar
%wealth keeps track of wealth EACH day

%the protfolio for the first day
Weight(1, :) = ones(1, num_stock) * (1/num_stock);

%from the second day to to the last day
for i = 2 : num_days
    fprintf('Day: %d\n', i);
    day_index = i - 1;
    t = Weight(day_index, :) .* M(day_index, :);
    %t is the scalar dot product of weight and data row vectors indexed at day_index
    Weight(i, :) = Weight(day_index, :) .* exp(eta * M(day_index, :) / t);
    Weight(i, :) = Weight(i, :) / sum(Weight(i, :));

    wealth(i,1) = wealth(i-1,1)*(Weight(i,:)*M(i,:)');
end
