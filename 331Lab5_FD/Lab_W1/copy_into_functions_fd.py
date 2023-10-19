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

        # TODO: define the integer number of mesh points, including boundaries, based on desired mesh spacing
        # self.nx =
        # self.nt =
        # self.n =

        # TODO: calculate the x and t values/coordinates of mesh as one-dimensional numpy arrays
        # self.x =
        # self.t =

        # TODO: calculate the actual mesh spacing in x and y, should be similar or same as the dx and dy arguments
        # self.dx =
        # self.dt =

        # set alpha, ratio of step sizes, and weight in implicit method
        self.alpha = alpha
        self.r = self.alpha*self.dt/(self.dx*self.dx)
        self.theta = theta

        # store the Dirichlet boundary conditions and initial conditions
        self.bc_x0 = bc_x0
        self.bc_x1 = bc_x1
        self.ic_t0 = ic_t0

        # TODO: initialise solution matrix, apply the Dirichlet boundary and initial conditions to it now
        # self.solution =

    def solve_explicit(self):
        """
        Solve the 1D heat equation using an explicit solution method.
        """
        # TODO: complete this method
        pass

    def implicit_update_a(self):
        """
        Set coefficients in the matrix A, prior to iterative solution. This only needs to be set once i.e. it doesn't
        change with each iteration, unlike the b vector.

        Returns:
            a (2D array): coefficient matrix for implicit method (dimension 2 n_x by 2 n_x)
        """
        # TODO: complete this method, ensure you return the matrix A.
        pass

    def implicit_update_b(self, indx_t):
        """
        Update the b vector for the current time step to be solved, making use of the

        Arguments:
            indx_t (int): time index for the current step being solved.

        Returns:
            b (1D array): vector of constants for implicit method (length of 2 n_x)
        """
        # TODO: complete this method, ensure you return the updated b.
        pass

    def solve_implicit(self):
        """
        Solve the 1D heat equation using an implicit solution method.
        """
        # TODO: complete this method. Recall you only need to set A once, though b must be updated each time step.
        pass


    def plot_solution(self, times=None, save_to_file=False, save_file_name='fig_HeatXT.png'):
        """
        Plot the solution as a 1D line plot of x(t) at regularly spaced specific times.

        Arguments:
            times (1D array): times (or time indexes) at which to plot the solution.
            save_to_file (boolean): if true, save the plot to a file with pre-determined name.
            save_file_name (string): name of figure to save if save_to_file is true.
        """
        # TODO: complete this method
        pass
