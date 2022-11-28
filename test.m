clear all
close all
clc

t0 = 0;
tfinal = 15;
y0 = [40; 10; 10];   
[t,y] = ode23(@lotka_new,[t0 tfinal],y0);

plot(t,y)
title('Predator/Prey Populations Over Time')
xlabel('t')
ylabel('Population')
legend('Prey','Predators 1', 'Predators 2', 'Location','North')