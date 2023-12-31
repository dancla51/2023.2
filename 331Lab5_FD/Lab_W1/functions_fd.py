# import statements
import random

import numpy as np
import matplotlib.pyplot as plt


class SolverPoissonXY(object):
    """
    Class containing attributes and methods for solving the Poisson/Laplace PDE in 2D Cartesian coordinates. Assumes
    rectangular model domain and boundary conditions defined along those.

    Attributes:
        nx (int): number of mesh points along the x dimension.
        ny (int): number of mesh points along the y dimension.
        n (int): total number of mesh points.
        x (1D array): mesh coordinates along the x dimension.
        y (1D array): mesh coordinates along the y dimension.
        dx (float): mesh spacing along the x dimension. May differ from input delta.
        dy (float): mesh spacing along the y dimension. May differ from input delta.
        bc_x0 (dict): type and equation for left boundary u(x0,y).
        bc_x1 (dict): type and equation for right boundary u(x1,y).
        bc_y0 (dict): type and equation for bottom boundary u(x,y0).
        bc_y1 (dict): type and equation for top boundary u(x,y1).
        poisson (callable): Poisson function.
        a (2D array): coefficient matrix in system of equations to solve for PDE solution.
        b (1D array): vector of constants in system of equations to solve for PDE solution.
        solution (2D array): PDE solution array on the mesh.
    """

    def __init__(self, xlim, ylim, delta, bc_x0, bc_x1, bc_y0, bc_y1, poisson):
        """
        Arguments:
            xlim (1D array): lower and upper limits in x dimension.
            ylim (1D array): lower and upper limits in y dimension.
            delta (float): desired mesh spacing in x and y dimension i.e. assume uniform mesh spacing
            bc_x0 (dict): type and equation for left boundary u(x0,y).
            bc_x1 (dict): type and equation for right boundary u(x1,y).
            bc_y0 (dict): type and equation for bottom boundary u(x,y0).
            bc_y1 (dict): type and equation for top boundary u(x,y1).
            poisson (callable): Poisson function.
        """
        self.nx = round((xlim[1]-xlim[0]) / delta) + 1
        self.ny = round((ylim[1]-ylim[0]) / delta) + 1
        self.n = self.nx * self.ny
        # X and Y vals
        self.x = np.linspace(xlim[0], xlim[1], self.nx)
        self.y = np.linspace(ylim[0], ylim[1], self.ny)

        self.dx = (xlim[1]-xlim[0]) / self.nx
        self.dy = (ylim[1]-ylim[0]) / self.ny

        self.a = np.zeros([self.n, self.n])
        '''for r in range(self.n):
            if r == 0:
                pass
            elif r == self.n-1:
                pass'''

        self.b = np.zeros([self.n])
        self.solution = np.zeros([self.nx, self.ny])

        # store the four boundary conditions
        self.bc_x0 = bc_x0
        self.bc_x1 = bc_x1
        self.bc_y0 = bc_y0
        self.bc_y1 = bc_y1

        # equation corresponding to forcing function
        self.poisson = poisson

    def dirichlet(self):
        """
        Update the corresponding elements of the A matrix and b vector for Dirichlet boundary mesh points.
        """
        if self.bc_y0.get("type")=="dirichlet":
            # Bottom edge
            y = self.y[0]
            # for each edge point
            for i in range(self.nx):
                x = self.x[i]
                # b
                self.b[i] = self.bc_y0.get("function")(x, y)
                # a
                self.a[i, i] = 1

        if self.bc_y1.get("type")=="dirichlet":
            # Top edge
            y = self.y[-1]
            # for each edge point
            for i in range(self.nx):
                x = self.x[i]
                # b
                self.b[self.nx*(self.ny-1)+i] = self.bc_y1.get("function")(x, y)
                # a
                self.a[self.nx*(self.ny-1)+i, self.nx*(self.ny-1)+i] = 1

        if self.bc_x0.get("type")=="dirichlet":
            # Left edge
            x = self.x[0]
            # for each edge point
            for j in range(self.ny):
                y = self.y[j]
                # b
                self.b[j*self.nx] = self.bc_x0.get("function")(x, y)
                # a
                self.a[j*self.nx, j*self.nx] = 1

        if self.bc_x1.get("type") == "dirichlet":
            # Right edge
            x = self.x[-1]
            # for each edge point
            for j in range(self.ny):
                y = self.y[j]
                # b
                self.b[j * self.nx + self.nx - 1] = self.bc_x1.get("function")(x, y)
                # a
                self.a[j * self.nx + self.nx - 1, j * self.nx + self.nx - 1] = 1

    def neumann(self):
        """
        Update the corresponding elements of the A matrix and b vector for Neumann boundary mesh points.
        """
        if self.bc_y0.get("type") == "neumann":
            # Bottom edge
            y = self.y[0]
            # for each edge point
            for i in range(1, self.nx-1):
                # a
                self.a[i, i] = -2 / self.dx / self.dx - 2 / self.dy / self.dy
                self.a[i, i - 1] = 1 / self.dx / self.dx
                self.a[i, i + 1] = 1 / self.dx / self.dx
                self.a[i, i + self.nx] = 2 / self.dy / self.dy
                # b
                x = self.x[i]
                self.b[i] = self.poisson(x, y) + 2 * self.bc_y0.get("function")(x, y) / self.dy

        if self.bc_y1.get("type") == "neumann":
            # Top edge
            y = self.y[-1]
            # for each edge point
            for i in range(1, self.nx-1):
                # a
                k = self.nx*(self.ny-1)+i
                self.a[k, k] = -2 / self.dx / self.dx - 2 / self.dy / self.dy
                self.a[k, k - 1] = 1 / self.dx / self.dx
                self.a[k, k + 1] = 1 / self.dx / self.dx
                self.a[k, k - self.nx] = 2 / self.dy / self.dy
                # b
                x = self.x[i]
                self.b[k] = self.poisson(x, y) - 2 * self.bc_y1.get("function")(x, y) / self.dy

        if self.bc_x0.get("type") == "neumann":
            # Left edge
            x = self.x[0]
            # for each edge point
            for j in range(1, self.ny-1):
                # a
                k = j * self.nx
                self.a[k, k] = -2 / self.dx / self.dx - 2 / self.dy / self.dy
                self.a[k, k + 1] = 2 / self.dy / self.dy
                self.a[k, k - self.nx] = 1 / self.dx / self.dx
                self.a[k, k + self.nx] = 1 / self.dx / self.dx
                # b
                y = self.y[j]
                self.b[k] = self.poisson(x, y) + 2 * self.bc_x0.get("function")(x, y) / self.dx

        if self.bc_x1.get("type") == "neumann":
            # Right edge
            x = self.x[-1]
            # for each edge point
            for j in range(1, self.ny-1):
                # a
                k = self.nx - 1 + j * self.nx
                self.a[k, k] = -2 / self.dx / self.dx - 2 / self.dy / self.dy
                self.a[k, k - 1] = 2 / self.dy / self.dy
                self.a[k, k - self.nx] = 1 / self.dx / self.dx
                self.a[k, k + self.nx] = 1 / self.dx / self.dx
                # b
                y = self.y[j]
                self.b[k] = self.poisson(x, y) - 2 * self.bc_x1.get("function")(x, y) / self.dx

        # DOES NOT ACCOUNT FOR TWO NEUMANN CONDITIONS ON ADJACENT EDGES


    def internal(self):
        """
        Update the corresponding elements of the A matrix and b vector for internal mesh points.
        """
        # Loop through each internal point
        for i in range(1, self.nx-1):
            for j in range(1, self.ny-1):
                # K is number of 1D-sol / B / column of A
                k = i + j * self.nx
                self.a[k, k] = -2 / self.dx / self.dx - 2 / self.dy / self.dy
                self.a[k, k - 1] = 1 / self.dx / self.dx
                self.a[k, k + 1] = 1 / self.dx / self.dx
                self.a[k, k - self.nx] = 1 / self.dy / self.dy
                self.a[k, k + self.nx] = 1 / self.dy / self.dy
                x = self.x[i]
                y = self.y[j]
                self.b[k] = self.poisson(x, y)

    def solve(self):
        """
        Call the dirichlet, neumann and internal methods to form the system of equations, Au=b. Then use built-in
        linear algebra solver to find u and reshape back to self.solution.
        """
        self.neumann()
        self.dirichlet()
        self.internal()
        # Solve
        u = np.linalg.solve(self.a, self.b)
        self.solution = np.reshape(u, (self.ny, self.nx))


    def plot_solution(self):
        """
        Plot the PDE solution.
        """
        X, Y = np.meshgrid(self.x, self.y)
        Z = self.solution

        # plot
        fig, ax = plt.subplots()
        contour = ax.contour(X, Y, Z, levels=20)
        ax.clabel(contour, fontsize=12)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Poisson Equation Solution for given boundary conditions")
        #plt.savefig("task1_delta="+str(round(self.dx,2))+".jpg")
        plt.show()


class SolverHeatXT(object):
    """
    Class containing attributes and methods for solving the 1D heat equation. Requires Dirichlet boundary conditions.

    Attributes:
        nx (int): number of mesh points along the spatial dimension.
        nt (int): number of mesh points along the time dimension.
        n (int): total number of mesh points.
        x (1D array): mesh coordinates along the x dimension.
        t (1D array): mesh coordinates along the t dimension.
        dx (float): mesh spacing along the x dimension.
        dt (float): mesh spacing along the t dimension.
        alpha (float): thermal diffusivity in the heat equation.
        r (float): equal to alpha*dt/(dx^2), useful for diagnosing numerical stability.
        theta (float): weight applied to spatial derivative at t^(n+1), where 0 < theta <= 1.
        bc_x0 (dict): dictionary storing information for left boundary conditions.
        bc_x1 (dict): dictionary storing information for right boundary conditions.
        ic_t0 (dict): dictionary storing information for initial conditions.
        solution (2D array): solution array corresponding to mesh dimensions (nx, nt).

    Arguments:
        xlim (1D array): lower and upper limits in x dimension.
        tlim (1D array): lower and upper limits in t dimension.
        dx (float): desired mesh spacing in x dimension. May not exactly equal set mesh spacing.
        dt (float): desired mesh spacing in t dimension. May not exactly equal set mesh spacing.
        bc_x0 (dict): boundary conditions along x0.
        bc_x1 (dict): boundary conditions along x1.
        ic_t0 (dict): initial conditions at t0.
        alpha (float): thermal diffusivity in the heat equation.
        theta (float): weight applied to spatial derivative at t^(n+1), where 0 < theta <= 1.
    """

    def __init__(self, xlim, tlim, dx, dt, alpha, theta, bc_x0, bc_x1, ic_t0):

        self.nx = round((xlim[1] - xlim[0]) / dx) + 1
        self.nt = round((tlim[1] - tlim[0]) / dt) + 1
        self.n = self.nx * self.nt

        self.x = np.linspace(xlim[0], xlim[1], self.nx)
        self.t = np.linspace(tlim[0], tlim[1], self.nt)

        self.dx = (xlim[1] - xlim[0]) / self.nx
        self.dt = (tlim[1] - tlim[0]) / self.nt

        # set alpha, ratio of step sizes, and weight in implicit method
        self.alpha = alpha
        self.r = self.alpha*self.dt/(self.dx*self.dx)
        self.theta = theta

        # store the Dirichlet boundary conditions and initial conditions
        self.bc_x0 = bc_x0
        self.bc_x1 = bc_x1
        self.ic_t0 = ic_t0

        # initialise solution matrix, apply the Dirichlet boundary and initial conditions to it now
        self.solution = np.zeros([self.nx, self.nt])
        # apply soln for bcs
        if self.bc_x0.get("type")=="dirichlet":
            # Left edge
            x = self.x[0]
            # for each edge point
            for s in range(self.nt):
                t = self.t[s]
                self.solution[0, s] = self.bc_x0.get("function")(x, t)
        if self.bc_x1.get("type") == "dirichlet":
            # Right edge
            x = self.x[-1]
            # for each edge point
            for s in range(self.nt):
                t = self.t[s]
                self.solution[-1, s] = self.bc_x1.get("function")(x, t)
        # Apply soln for ICs
        if self.ic_t0.get("type")=="initial":
            # 'Bottom' edge
            t = self.t[0]
            # for each edge point
            for i in range(self.nx):
                x = self.x[i]
                self.solution[i, 0] = self.ic_t0.get("function")(x, t)



    def solve_explicit(self):
        """
        Solve the 1D heat equation using an explicit solution method.
        """
        # Explicit method
        for n in range(self.nt-1):
            for i in range(1, self.nx-1):
                # Solve point
                self.solution[i, n+1] = self.r * self.solution[i-1, n] + (1-2*self.r)*self.solution[i, n] + self.r*self.solution[i+1, n]


    def implicit_update_a(self):
        """
        Set coefficients in the matrix A, prior to iterative solution. This only needs to be set once i.e. it doesn't
        change with each iteration, unlike the b vector.

        Returns:
            a (2D array): coefficient matrix for implicit method (dimension 2 n_x by 2 n_x)
        """
        # returns A matrix
        a = np.zeros([self.nx*2, self.nx*2])
        for k in range(self.nx*2):
            if (k <= self.nx or k == self.nx*2-1) :
                a[k, k] = 1
            else:
                # from this timestep
                a[k, k - 1] = self.theta * self.r
                a[k, k] = -1 * (1+2*self.theta*self.r)
                a[k, k + 1] = self.theta * self.r
                # from previous timestep
                a[k, k - 1 - self.nx] = (1-self.theta) * self.r
                a[k, k - self.nx] = 1 - 2*(1-self.theta)*self.r
                a[k, k + 1 - self.nx] = (1-self.theta) * self.r
        return a

    def implicit_update_b(self, indx_t):
        """
        Update the b vector for the current time step to be solved, making use of the

        Arguments:
            indx_t (int): time index for the current step being solved.

        Returns:
            b (1D array): vector of constants for implicit method (length of 2 n_x)
        """
        # complete this method, ensure you return the updated b.
        b = np.zeros([self.nx*2])
        for k in range(self.nx*2):
            # top half from prev iteration / IC
            if k < self.nx:
                b[k] = self.solution[k, indx_t-1]
            elif (k==self.nx or k==2*self.nx-1):
                # BCs
                b[k] = self.solution[k-self.nx, indx_t]
        return b

    def solve_implicit(self):
        """
        Solve the 1D heat equation using an implicit solution method.
        """
        # TODO: complete this method. Recall you only need to set A once, though b must be updated each time step.
        a = self.implicit_update_a()
        for indx_t in range(1, self.nt):
            b = self.implicit_update_b(indx_t)
            sol = np.linalg.solve(a, b)
            # Take bottom half of solution vector
            self.solution[:,indx_t] = sol[self.nx:]



    def plot_solution(self, times=None, save_to_file=False, save_file_name='fig_HeatXT.png'):
        """
        Plot the solution as a 1D line plot of x(t) at regularly spaced specific times.

        Arguments:
            times (1D array): times (or time indexes) at which to plot the solution.
            save_to_file (boolean): if true, save the plot to a file with pre-determined name.
            save_file_name (string): name of figure to save if save_to_file is true.
        """
        # TODO: complete this method
        nplots = 4
        fig, ax = plt.subplots(nplots, 1)

        mult = np.floor(self.nt / (nplots))
        for ind, time in enumerate(np.linspace(self.t[0], self.t[-1], nplots)):
            ax[ind].plot(self.x, self.solution[:, round(ind*mult)])
            ax[ind].set_title("Time = %.2f s" % time, x=0.5, y=0.6)
            ax[ind].set_xlabel("x")
            ax[ind].set_ylabel("Temperature")

        fig.suptitle('Solution behaviour over time for heat system ('+save_file_name+')')
        if save_to_file:
            plt.savefig(fname=save_file_name+".jpg")
        else:
            plt.show()


