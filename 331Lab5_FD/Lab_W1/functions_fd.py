# import statements
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
        # TODO: define the integer number of mesh points, including boundaries, based on desired mesh spacing
        self.nx = round((xlim[1]-xlim[0]) / delta)
        self.ny = round((ylim[1]-ylim[0]) / delta)
        self.n = self.nx * self.ny

        # TODO: calculate the x and y values/coordinates of mesh as one-dimensional numpy arrays
        self.x = np.array([])
        self.y = np.array([])
        for x in range()

        # TODO: calculate the actual mesh spacing in x and y, may not be same as delta if not exactly divisible
        self.dx = (xlim[1]-xlim[0]) / self.nx
        self.dy = (ylim[1]-ylim[0]) / self.ny

        # TODO: initialise the linear algebra matrices for, A solution = b
        # self.a =
        # self.b =
        # self.solution =

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
        pass

    def neumann(self):
        """
        Update the corresponding elements of the A matrix and b vector for Neumann boundary mesh points.
        """
        pass

    def internal(self):
        """
        Update the corresponding elements of the A matrix and b vector for internal mesh points.
        """
        pass

    def solve(self):
        """
        Call the dirichlet, neumann and internal methods to form the system of equations, Au=b. Then use built-in
        linear algebra solver to find u and reshape back to self.solution.
        """
        pass

    def plot_solution(self):
        """
        Plot the PDE solution.
        """
