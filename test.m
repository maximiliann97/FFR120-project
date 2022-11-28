clear all
close all
clc
syms x(t) y(t) z(t)
a = 0.01;
b = 0.02;
c = 1;

ode1 = diff(x) == a*x + x*y - x*z;
ode2 = diff(y) == -b*y + x*y;
ode3 = diff(z) == -c*z + x*z;

odes = [ode1; ode2; ode3];

S = dsolve(odes)