import numpy as np
import matplotlib.pyplot as plt
from functions2 import f6, f7
from newton_multi import newton_multi

## Task 5

# initialisation
tol = 1.0e-8;             # numerical tolerance
h = 1.0e-4;               # step size for central difference
max_iter = 50;            # maximum number of iterations
n = 2;                    # number of variables / equations
x0_p = []                 # declare initial root estimate dictionary
x0_p.append([-1.0,3.0])   # initial root estimate - point 1
x0_p.append([2.0,3.0])    # initial root estimate - point 2
x0_p.append([2.0,0.0])    # initial root estimate - point 3
func = f6

num_points=len(x0_p)

# Two function two variable Newton's method for each starting location
xn_p={}
for i in range(num_points):
    xn_p[i],exit_flag = newton_multi(n, func, x0_p[i], h, max_iter, tol);

# Need to create arrays for x and y axes for each line
k={}
for i in range(num_points):
    k[i] = range(len(xn_p[i]))

# Create our 1d arrays of function values at (x1_k,x2_k)
fval={}
for i in range(num_points):
    fval[i]={}
    for j in range(n):
        fval[i][j]=np.zeros(len(xn_p[i]))

for i in range(num_points):
    for kk in k[i]:
        f_temp=func(xn_p[i][kk])
        for j in range(n):
            fval[i][j][kk]=f_temp[j]

fig, ax = plt.subplots(nrows=2,ncols=1)
for i in range(num_points):
    for j in range(n):
        ax[j].plot(k[i], fval[i][j], label=f'$(x_0,y_0)={x0_p[i]}$')

for j in range(n):
    ax[j].legend()
    ax[j].set_ylabel(f'$f_{j}(x^k)$')
ax[1].set_xlabel('$k$')
plt.show()


# create a pair of 3d plots one for each function
x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(x, y)
Z0 = np.array([[func([X[i,j],Y[i,j]])[0] for i in range(len(x))] for j in range(len(y))])
Z1 = np.array([[func([X[i,j],Y[i,j]])[1] for i in range(len(x))] for j in range(len(y))])

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')

surf = ax.plot_surface(X, Y, Z0, cmap=plt.cm.autumn,
                           linewidth=0, antialiased=True, alpha=0.4)

ax2 = fig.add_subplot(1, 2, 2, projection='3d')

surf = ax2.plot_surface(X, Y, Z1, cmap=plt.cm.winter,
                           linewidth=0, antialiased=True,alpha=0.4)

for i in range(num_points):
    ax.scatter([xn_p[i][kk][1] for kk in k[i]],[xn_p[i][kk][0] for kk in k[i]],fval[i][0], label=f'$f_0(x_k,y_k); (x_0,y_0)={x0_p[i]}$')
    ax2.scatter([xn_p[i][kk][1] for kk in k[i]],[xn_p[i][kk][0] for kk in k[i]],fval[i][1], label=f'$f_1(x_k,y_k); (x_0,y_0)={x0_p[i]}$')
    ax.plot([xn_p[i][kk][1] for kk in k[i]],[xn_p[i][kk][0] for kk in k[i]],fval[i][0], label=f'$f_0(x_k,y_k); (x_0,y_0)={x0_p[i]}$')
    ax2.plot([xn_p[i][kk][1] for kk in k[i]],[xn_p[i][kk][0] for kk in k[i]],fval[i][1], label=f'$f_1(x_k,y_k); (x_0,y_0)={x0_p[i]}$')

ax.legend()
ax2.legend()

def on_move(event):
    if event.inaxes == ax:
        ax2.view_init(elev=ax.elev, azim=ax.azim)
    elif event.inaxes == ax2:
        ax.view_init(elev=ax2.elev, azim=ax2.azim)
    else:
        return
    fig.canvas.draw_idle()

c1 = fig.canvas.mpl_connect('motion_notify_event', on_move)


plt.show()
