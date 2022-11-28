function yp = lotka_new(t,y)
    % Parameters need to be changed, these are arbitrary
    a = 0.01;   % exponential growth rate of the prey
    b = 0.02;   % decline rate in the prey population due to predation
    c = 0.03;   % exponential decline in population of predator 1
    d = 0.04;   % growth rate in predator 1 population resulting from predation
    e = 0.05;   % exponential decline in population of predator 2
    f = 0.06;   % growth rate in predator 2 population resulting from predation
    
    
    yp = diag([a - b*y(2) - b*y(3), -c + d*y(1), -e + f*y(1)])*y;
end