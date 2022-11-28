function yp = lotka_new(t,y)
    yp = diag([1 - .01*y(2), -1 + .02*y(1), -0.004 + y(1)])*y;
end