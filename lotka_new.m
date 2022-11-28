function yp = lotka_new(t,y)
    a = 1;
    b = 2;
    c = 3;
    yp = diag([a - y(2) - y(3), -b + y(1), -c + y(1)])*y;
end