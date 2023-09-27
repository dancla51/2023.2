## Task 3: Sensitivity of Newton's method

from core import *
import cmath
import numpy
import matplotlib.pyplot as plt

from algorithms import newton_damped

def fx(x):
    return x**6-1

def gx(x):
    return 6*x**5

roots = {}

n = 200                     # resolution (2*n+1 by 2*n+1 grid of sample points)
beta = 0                    # damping factor
extent=[-1,1,-1,1]  # format: [real_min,real_max,imag_min,imag_max]

complete = numpy.zeros((2*n+1,2*n+1))
iterations = numpy.zeros((2*n+1,2*n+1))
stepx=(extent[1]-extent[0])/(2*n)
stepy=(extent[3]-extent[2])/(2*n)

# Define sqrt(-1)
j = (-1)**(0.5)

# Loop through starting points and find converged solutions
for a in range(2*n+1):
    aa=a*stepx+extent[0]
    for b in range(2*n+1):
        if complete[2*n-b,a]!=0:
            continue
        bb=b*stepy+extent[2]
        
        x, iter, exit_flag = newton_damped(fx,gx,aa+j*bb,100,0.0001,beta)
        if exit_flag==ExitFlag.Converged:
            x_round=round(x[-1].real,3) + round(x[-1].imag,3)*j
            if x_round not in roots:
                roots[x_round]=len(roots)+1
            
            for i in range(len(x)):
                p = round((x[i].real-extent[0])/stepx)
                q = round((x[i].imag-extent[2])/stepy)
                if p>=0 and q>=0 and p<=2*n and q<=2*n and complete[2*n-q,p]==0:
                    complete[2*n-q,p]=roots[x_round]
                    iterations[2*n-q,p]=iter-i
                else:
                    break 

# Create plots
fig, ax = plt.subplots(1, 2, figsize=(16, 7))
ax[0].imshow(complete, interpolation='bilinear',extent=extent)
ax[1].imshow(iterations, interpolation='bilinear',extent=extent)

plt.show()


