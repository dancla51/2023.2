# Initialisation 
import numpy as np
import matplotlib.pyplot as plt
import core
from algorithms import bisection, secant, regula_falsi, newton, combined
from functions import f2, g2, f3, g3, f4, g4

plt.rcParams.update({
    "text.usetex": False})

tol = 1.0e-4  # tolerance
max_iter = 20 # maximum number of iterations

# initial root estimates / intervals for each function
# column 1: x0 for initial bracket methods
# column 2: x1 for initial bracket methods
# column 3: x0 for Newton's method
xint1 = ([-3.0,0.5,-3.0]);
xint2 = ([-5.,2.,1.1]);
xint3 = ([-2.0,1.5,-0.40]);

# function titles for plots
title1 = '$f_2(x)=x^2-1$';
title2 = '$f_3(x)=(e^x - e^{-x})/(e^x + e^{-x})$';
title3 = '$f_4(x)=cos(x)+sin(x^2)$';

# set to false when you don't need to produce plot of functions
disp_func = True
if disp_func:
    x = np.linspace(-5.,5.,1000);

    fig, ax = plt.subplots(nrows=3,ncols=1)
    line1, = ax[0].plot(x, [f2(x1) for x1 in x], label='F2')
    line2, = ax[1].plot(x, [f3(x1) for x1 in x], label='F3')
    line3, = ax[2].plot(x, [f4(x1) for x1 in x], label='F4')
    ax[0].set_title(title1)
    ax[1].set_title(title2)
    ax[2].set_title(title3)
    ax[2].set_xlabel('$x$')
    ax[0].grid(True)
    ax[1].grid(True)
    ax[2].grid(True)
    fig.tight_layout()
    fig.canvas.set_window_title('Plots of functions') 
    plt.show()

# bisection method
xbf2 = bisection(f2, xint1[0], xint1[1], max_iter, tol)
xbf3 = bisection(f3, xint2[0], xint2[1], max_iter, tol)
xbf4 = bisection(f4, xint3[0], xint3[1], max_iter, tol)
print('Bisection method')
print('f2: '+str(xbf2[2]))
print('f3: '+str(xbf3[2]))
print('f4: '+str(xbf4[2]))
print('')

# secant method
xsf2 = secant(f2, xint1[0], xint1[1], max_iter, tol)
xsf3 = secant(f3, xint2[0], xint2[1], max_iter, tol)
xsf4 = secant(f4, xint3[0], xint3[1], max_iter, tol)
print('Secant method')
print('f2: '+str(xsf2[2]))
print('f3: '+str(xsf3[2]))
print('f4: '+str(xsf4[2]))
print('')

## regula falsi method
xrf2 = regula_falsi(f2, xint1[0], xint1[1], max_iter, tol)
xrf3 = regula_falsi(f3, xint2[0], xint2[1], max_iter, tol)
xrf4 = regula_falsi(f4, xint3[0], xint3[1], max_iter, tol)
print('Regula falsi method')
print('f2: '+str(xrf2[2]))
print('f3: '+str(xrf3[2]))
print('f4: '+str(xrf4[2]))
print('')

# Newton's method
xnf2 = newton(f2, g2, xint1[2], max_iter, tol)
xnf3 = newton(f3, g3, xint2[2], max_iter, tol)
xnf4 = newton(f4, g4, xint3[2], max_iter, tol)
print('Newton method')
print('f2: '+str(xnf2[2]))
print('f3: '+str(xnf3[2]))
print('f4: '+str(xnf4[2]))
print('')

# combined bisection/newtons method
xcf2 = combined(f2, g2, xint1[0], xint1[1], max_iter, tol)
xcf3 = combined(f3, g3, xint2[0], xint2[1], max_iter, tol)
xcf4 = combined(f4, g4, xint3[0], xint3[1], max_iter, tol)
print('Combined bisection / Newton method')
print('f2: '+str(xcf2[2]))
print('f3: '+str(xcf3[2]))
print('f4: '+str(xcf4[2]))
print('')

## start figure for method root estimate comparison
fig, ax = plt.subplots(nrows=3,ncols=1)

## create top plot for f2
ax[0].plot(np.linspace(1,len(xbf2[0]),len(xbf2[0])), xbf2[0], label='Bisection: '+str(len(xbf2[0]))+' estimates')
ax[0].plot(np.linspace(1,len(xsf2[0]),len(xsf2[0])), xsf2[0], label='Secant: '+str(len(xsf2[0]))+' estimates')
ax[0].plot(np.linspace(1,len(xrf2[0]),len(xrf2[0])), xrf2[0], label='Regula Falsi: '+str(len(xrf2[0]))+' estimates')
ax[0].plot(np.linspace(1,len(xnf2[0]),len(xnf2[0])), xnf2[0], label='Newton: '+str(len(xnf2[0]))+' estimates')
ax[0].plot(np.linspace(1,len(xcf2[0]),len(xcf2[0])), xcf2[0], label='Combined: '+str(len(xcf2[0]))+' estimates')
box = ax[0].get_position()
ax[0].set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

## create middle plot for f3
ax[1].plot(np.linspace(1,len(xbf3[0]),len(xbf3[0])), xbf3[0], label='Bisection: '+str(len(xbf3[0]))+' estimates')
ax[1].plot(np.linspace(1,len(xsf3[0]),len(xsf3[0])), xsf3[0], label='Secant: '+str(len(xsf3[0]))+' estimates')
ax[1].plot(np.linspace(1,len(xrf3[0]),len(xrf3[0])), xrf3[0], label='Regula Falsi: '+str(len(xrf3[0]))+' estimates')
ax[1].plot(np.linspace(1,len(xnf3[0]),len(xnf3[0])), xnf3[0], label='Newton: '+str(len(xnf3[0]))+' estimates')
ax[1].plot(np.linspace(1,len(xcf3[0]),len(xcf3[0])), xcf3[0], label='Combined: '+str(len(xcf3[0]))+' estimates')
box = ax[1].get_position()
ax[1].set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

## create bottom plot for f4
ax[2].plot(np.linspace(1,len(xbf4[0]),len(xbf4[0])), xbf4[0], label='Bisection: '+str(len(xbf4[0]))+' estimates')
ax[2].plot(np.linspace(1,len(xsf4[0]),len(xsf4[0])), xsf4[0], label='Secant: '+str(len(xsf4[0]))+' estimates')
ax[2].plot(np.linspace(1,len(xrf4[0]),len(xrf4[0])), xrf4[0], label='Regula Falsi: '+str(len(xrf4[0]))+' estimates')
ax[2].plot(np.linspace(1,len(xnf4[0]),len(xnf4[0])), xnf4[0], label='Newton: '+str(len(xnf4[0]))+' estimates')
ax[2].plot(np.linspace(1,len(xcf4[0]),len(xcf4[0])), xcf4[0], label='Combined: '+str(len(xcf4[0]))+' estimates')
box = ax[2].get_position()
ax[2].set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax[0].set_ylabel('$x_2(x)$')
ax[1].set_ylabel('$x_3(x)$')
ax[2].set_ylabel('$x_4(x)$')
ax[2].set_xlabel('$k^{th}$ Root Estimate')
ax[0].grid(True)
ax[1].grid(True)
ax[2].grid(True)
fig.tight_layout()
fig.canvas.set_window_title('Root estimates') 
plt.show()

## end figure for method root estimate comparison

## start figure for method performance comparison
fig, ax = plt.subplots(nrows=3,ncols=2)

ax[0,0].plot(np.linspace(1,len(xbf2[0]),len(xbf2[0])),[abs(f2(x)) for x in xbf2[0]], label='Bisection')
ax[0,0].plot(np.linspace(1,len(xsf2[0]),len(xsf2[0])),[abs(f2(x)) for x in xsf2[0]], label='Secant')
ax[0,0].plot(np.linspace(1,len(xrf2[0]),len(xrf2[0])),[abs(f2(x)) for x in xrf2[0]], label='Regula Falsi')
ax[0,0].plot(np.linspace(1,len(xnf2[0]),len(xnf2[0])),[abs(f2(x)) for x in xnf2[0]], label='Newton')
ax[0,0].plot(np.linspace(1,len(xcf2[0]),len(xcf2[0])),[abs(f2(x)) for x in xcf2[0]], label='Combined')

ax[0,1].plot(np.linspace(1,len(xbf2[0]),len(xbf2[0])),[abs(x+1) for x in xbf2[0]], label='Bisection')
ax[0,1].plot(np.linspace(1,len(xsf2[0]),len(xsf2[0])),[abs(x-1) for x in xsf2[0]], label='Secant')
ax[0,1].plot(np.linspace(1,len(xrf2[0]),len(xrf2[0])),[abs(x+1) for x in xrf2[0]], label='Regula Falsi')
ax[0,1].plot(np.linspace(1,len(xnf2[0]),len(xnf2[0])),[abs(x+1) for x in xnf2[0]], label='Newton')
ax[0,1].plot(np.linspace(1,len(xcf2[0]),len(xcf2[0])),[abs(x+1) for x in xcf2[0]], label='Combined')

ax[1,0].plot(np.linspace(1,len(xbf3[0]),len(xbf3[0])),[abs(f3(x)) for x in xbf3[0]], label='Bisection')
ax[1,0].plot(np.linspace(1,len(xsf3[0]),len(xsf3[0])),[abs(f3(x)) for x in xsf3[0]], label='Secant')
ax[1,0].plot(np.linspace(1,len(xrf3[0]),len(xrf3[0])),[abs(f3(x)) for x in xrf3[0]], label='Regula Falsi')
ax[1,0].plot(np.linspace(1,len(xnf3[0]),len(xnf3[0])),[abs(f3(x)) for x in xnf3[0]], label='Newton')
ax[1,0].plot(np.linspace(1,len(xcf3[0]),len(xcf3[0])),[abs(f3(x)) for x in xcf3[0]], label='Combined')

ax[1,1].plot(np.linspace(1,len(xbf3[0]),len(xbf3[0])),[abs(x) for x in xbf3[0]], label='Bisection')
ax[1,1].plot(np.linspace(1,len(xsf3[0]),len(xsf3[0])),[abs(x) for x in xsf3[0]], label='Secant')
ax[1,1].plot(np.linspace(1,len(xrf3[0]),len(xrf3[0])),[abs(x) for x in xrf3[0]], label='Regula Falsi')
ax[1,1].plot(np.linspace(1,len(xnf3[0]),len(xnf3[0])),[abs(x) for x in xnf3[0]], label='Newton')
ax[1,1].plot(np.linspace(1,len(xcf3[0]),len(xcf3[0])),[abs(x) for x in xcf3[0]], label='Combined')

ax[2,0].plot(np.linspace(1,len(xbf4[0]),len(xbf4[0])),[abs(f4(x)) for x in xbf4[0]], label='Bisection')
ax[2,0].plot(np.linspace(1,len(xsf4[0]),len(xsf4[0])),[abs(f4(x)) for x in xsf4[0]], label='Secant')
ax[2,0].plot(np.linspace(1,len(xrf4[0]),len(xrf4[0])),[abs(f4(x)) for x in xrf4[0]], label='Regula Falsi')
ax[2,0].plot(np.linspace(1,len(xnf4[0]),len(xnf4[0])),[abs(f4(x)) for x in xnf4[0]], label='Newton')
ax[2,0].plot(np.linspace(1,len(xcf4[0]),len(xcf4[0])),[abs(f4(x)) for x in xcf4[0]], label='Combined')

ax[2,1].plot(np.linspace(1,len(xbf4[0]),len(xbf4[0])),[abs(x+1.6054575755962381) for x in xbf4[0]], label='Bisection')
ax[2,1].plot(np.linspace(1,len(xsf4[0]),len(xsf4[0])),[abs(x-1.6054575755962381) for x in xsf4[0]], label='Secant')
ax[2,1].plot(np.linspace(1,len(xrf4[0]),len(xrf4[0])),[abs(x+1.6054575755962381) for x in xrf4[0]], label='Regula Falsi')
ax[2,1].plot(np.linspace(1,len(xnf4[0]),len(xnf4[0])),[abs(x+13.614448358230353) for x in xnf4[0]], label='Newton')
ax[2,1].plot(np.linspace(1,len(xcf4[0]),len(xcf4[0])),[abs(x+1.6054575755962381) for x in xcf4[0]], label='Combined')

for i in range(3):
    for j in range(2):
        ax[i,j].set_yscale('log')
        ax[i,j].grid(True)
        ax[i,j].legend()
        ax[i,j].set_xlabel('$k^{th}$ Root Estimate')   
        box = ax[i,j].get_position()
        ax[i,j].set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax[i,j].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
    ax[i,0].set_ylabel('$|f_'+str(i+2)+'(x^k)|$')
    ax[i,1].set_ylabel('$|x^k - \chi|$')
fig.tight_layout()
fig.canvas.set_window_title('Convergence comparison') 
plt.show()

## end figure for method performance comparison
