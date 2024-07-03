import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import gridspec
import matplotlib.tri as tri


class Diagram:
    """
    This is a base class for construction of diagrams.

    :ivar colours: Predefined set of colours
    :type colours: list[str]
    :ivar markers: Predefined set of markers
    :type markers: list[str]
    :ivar linestyles: Predefined set of linestyles
    :type linestyles: list[str]
    :ivar ax_labels: Axis labels
    :type ax_labels: list[str]
    """
    colours = ['blue', 'lightskyblue', 'mediumseagreen', 'orchid', 'dodgerblue', 'darkcyan']
    markers = [None, "--", "o", "v"]
    linestyles = ['solid', 'dashed']
    ax_labels = [None, None, None]

    def __init__(self, nrows: int = 1, ncols: int = 1, figsize: tuple = (8, 6)):
        """
        Constructor for Diagram base class

        :param nrows: Number of rows for subplots
        :type nrows: int
        :param ncols: Number of columns for subplots
        :type ncols: int
        :param figsize: Size of figure object
        :type figsize: tuple[float]
        """
        self.fig, self.ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        self.im = []

    def draw_surf(self, x, y, data: np.ndarray, levels: list = None, colours: list = None):
        """
        Function to draw 2D pcolormesh.

        :param x: Grid points on x-axis
        :type x: list
        :param y: Grid points on y-axis
        :type y: list
        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param colours: Colours for ListedColormap
        :type colours: list[str]
        """
        if colours is None:
            cmap = 'RdBu'
            # cmap = plt.get_cmap('RdBu', np.max(data) - np.min(data) + 1)
        elif isinstance(colours, list):
            cmap = colors.ListedColormap(colours)
        else:
            cmap = colours

        vmin = np.amin(data) * 0.999  # -10.1
        vmax = np.amax(data) * 1.001  # 10.1
        levels = np.linspace(vmin, vmax, 101) if levels is None else levels

        dx, dy = x[1]-x[0], y[1]-y[0]
        nx, ny = len(x), len(y)
        xgrid = np.linspace(x[0]-0.5*dx, x[-1]+0.5*dx, nx+1)
        ygrid = np.linspace(y[0]-0.5*dy, y[-1]+0.5*dy, ny+1)
        X, Y = np.meshgrid(xgrid, ygrid)
        z = np.swapaxes(data, 0, 1)
        self.im = self.ax.pcolormesh(X, Y, z, shading='flat', cmap=cmap, vmin=levels[0], vmax=levels[-1])
        self.ax.set(xlim=[x[0], x[-1]], ylim=[y[0], y[-1]])

        self.add_attributes(ax_labels=self.ax_labels)

        return

    def draw_contourmap(self, x, y, data: np.ndarray, levels: list = None, cmap: str = None, fill: bool = False):
        """
        Function to draw contourmap

        :param x: Grid points on x-axis
        :type x: list
        :param y: Grid points on y-axis
        :type y: list
        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param cmap: Colourmap name
        :type cmap: str
        :param fill: Switch for filled contours
        :type fill: bool
        """
        vmin = np.amin(data) * 0.999  # -10.1
        vmax = np.amax(data) * 1.001  # 10.1
        levels = np.linspace(vmin, vmax, 101) if levels is None else levels

        xgrid = np.linspace(x[0], x[-1], len(x))
        ygrid = np.linspace(y[0], y[-1], len(y))
        X, Y = np.meshgrid(xgrid, ygrid)
        z = np.swapaxes(data, 0, 1)

        if fill:
            self.im = self.ax.contourf(X, Y, z, cmap=cmap, vmin=levels[0], vmax=levels[-1])
        else:
            self.im = self.ax.contour(X, Y, z, cmap=cmap, vmin=levels[0], vmax=levels[-1])

        self.add_attributes(ax_labels=self.ax_labels)

        return

    def draw_line(self, x: list, y: list, z: list = None, color: str = None, label: str = None,
                  linestyle: str = None, line_size: float = None):
        """
        Function to draw line with coordinates X-Y(-Z)

        :param x: List of X-coordinates for line
        :type x: list
        :param y: List of Y-coordinates for line
        :type y: list
        :param z: List of Z-coordinates for line, optional
        :type z: list
        :param color: Line colour, optional
        :type color: str
        :param label: Line label
        :type label: str
        :param linestyle: Linestyle, default is 'solid'
        :type linestyle: str
        :param line_size: Line thickness
        :type line_size: float
        """
        linestyle = linestyle if linestyle is not None else self.linestyles[0]

        self.ax.plot(x, y, color=color, linestyle=linestyle, label=label)
        return

    def draw_point(self, X: list, Y: list, Z: list = None, color: str = None, marker: str = None,
                   point_size: float = 20):
        """
        Function to draw points with coordinates X-Y(-Z)

        :param X: List of X-coordinates for points
        :type X: list
        :param Y: List of Y-coordinates for points
        :type Y: list
        :param Z: List of Z-coordinates for points, optional
        :type Z: list
        :param color: Point colour, optional
        :type color: str
        :param marker: Marker style, optional
        :type marker: str
        :param point_size: Point size, optional
        :type point_size: float
        """
        for i, (x, y) in enumerate(zip(X, Y)):
            self.ax.scatter(x, y, c=color, s=pointsize, marker=marker)
        return

    def draw_contours(self, x, y, data: np.ndarray, colours: str = None, linewidth: float = 1.):
        """
        Function to draw contour lines between levels

        :param x: Grid points on x-axis
        :type x: list
        :param y: Grid points on y-axis
        :type y: list
        :param data: :class:`np.ndarray` of data for plotting
        :param colours: Colours for contourlines
        :type colours: str
        :param linewidth: Line width
        :type linewidth: float
        """
        dx, dy = x[1]-x[0], y[1]-y[0]
        nx, ny = len(x), len(y)
        colours = colours if colours is not None else self.colours

        # Find boundaries between discrete levels
        contours = {}
        levels = {}
        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                if i < nx-1 and data[i, j] != data[i + 1, j]:
                    pair = (min(data[i, j], data[i + 1, j]), max(data[i, j], data[i + 1, j]))

                    key = 0
                    for level in levels.values():
                        if level == pair:
                            break
                        key += 1
                    levels[key] = pair

                    if key in contours.keys():
                        contours[key] += [[(i + 1, i + 1), (j, j + 1)]]
                    else:
                        contours[key] = [[(i + 1, i + 1), (j, j + 1)]]
                if j < ny-1 and data[i, j] != data[i, j + 1]:
                    pair = (min(data[i, j], data[i, j + 1]), max(data[i, j], data[i, j + 1]))

                    key = 0
                    for level in levels.values():
                        if level == pair:
                            break
                        key += 1
                    levels[key] = pair

                    if key in contours.keys():
                        contours[key] += [[(i, i + 1), (j + 1, j + 1)]]
                    else:
                        contours[key] = [[(i, i + 1), (j + 1, j + 1)]]

        # Plot lines at the boundaries
        xgrid = np.linspace(x[0]-dx*0.5, x[-1]+dx*0.5, nx + 1)
        ygrid = np.linspace(y[0]-dy*0.5, y[-1]+dy*0.5, ny + 1)

        for ith_contour, (level, lines) in enumerate(contours.items()):
            colour = colours if isinstance(colours, str) else colours[ith_contour]
            for line in lines:
                x = [xgrid[line[0][0]], xgrid[line[0][1]]]
                y = [ygrid[line[1][0]], ygrid[line[1][1]]]
                self.ax.plot(x, y, c=colour, linewidth=linewidth)

        return

    def add_attributes(self, title: str = None, ax_labels: list = None, legend: bool = False,
                       colorbar: bool = False, ticks: list = None, grid: bool = False):
        """
        Function to add attributes to diagram.

        :param title: Figure title
        :type title: str
        :param ax_labels: Axes labels
        :type ax_labels: list[str]
        :param legend: Switch to add legend for lines/points
        :type legend: bool
        :param colorbar: Switch to add colorbar
        :type colorbar: bool
        """
        # add title, axlabels, legend, colorbar if not None
        if title:
            self.fig.suptitle(title)

        if ax_labels:
            self.ax.set_xlabel(ax_labels[0])
            self.ax.set_ylabel(ax_labels[1])

        if legend:
            self.ax.legend()

        if colorbar:
            plt.colorbar(self.im, ticks=ticks)

        if grid:
            self.ax.grid(True, which='both', linestyle='-.')
            self.ax.tick_params(direction='in', length=1, width=1, colors='k',
                                grid_color='k', grid_alpha=0.2)

        return


class Plot(Diagram):
    def draw_plot(self, xdata: list, ydata: list, number_of_curves: int = 1, title: str = None,
                  xlabel: str = None, ylabel: str = None, xlim: list = None, ylim: list = None,
                  logx: bool = False, logy: bool = False,datalabels: list = None, legend_loc: str = 'upper right'):
        xdata = [xdata] if not isinstance(xdata[0], (list, np.ndarray)) else xdata
        ydata = [ydata] if not isinstance(ydata[0], (list, np.ndarray)) else ydata

        plt.rc('font', size=16)
        self.ax.grid(True, which='both', linestyle='-.')
        self.ax.tick_params(direction='in', length=1, width=1, colors='k',
                            grid_color='k', grid_alpha=0.2)

        for i in range(number_of_curves):
            c = self.colours[i] if number_of_curves <= len(self.colours) else None
            plt.plot(xdata[i][:], ydata[i][:], c=c, linewidth=2,
                     label=datalabels[i] if datalabels is not None else None)

        if logx:
            plt.xscale("log")
        if logy:
            plt.yscale("log")

        plt.xlim(xlim if xlim is not None else None)
        plt.ylim(ylim if ylim is not None else None)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if datalabels is not None:
            plt.legend(loc=legend_loc)

    def draw_refdata(self, number_of_curves: int, xref: list, yref: list, reflabels: list = None):
        xref = [xref] if not isinstance(xref[0], (list, np.ndarray)) else xref
        yref = [yref] if not isinstance(yref[0], (list, np.ndarray)) else yref

        for i in range(number_of_curves):
            plt.scatter(xref[i][:], yref[i][:], c=self.colours[i], linewidth=2,
                        label=reflabels[i] if reflabels is not None else None)
        return


class PhaseDiagram(Diagram):
    """
    This class can construct P-T, P-x and T-x diagrams.
    """

    def Px(self, pressure: np.ndarray, Xi: np.ndarray, data: np.ndarray, levels: list = None, colours: list = None,
           contour: bool = False, fill: bool = False):
        """
        Function to draw P-x diagram.

        :param pressure: :class:`np.ndarray` of pressures
        :param Xi: :class:`np.ndarray` of compositions
        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param colours: Colours for cmap
        :type colours: list[str]
        :param contour: Switch for contour plot
        :type contour: bool
        :param fill: Switch for filled contour plot
        :type fill: bool
        """
        self.ax_labels = ["x", "Pressure, bar"]

        if contour:
            return self.draw_contourmap(x=Xi, y=pressure, data=data, levels=levels, fill=fill)
        else:
            return self.draw_surf(x=Xi, y=pressure, data=data, colours=colours, levels=levels)

    def Tx(self, temperature: np.ndarray, Xi: np.ndarray, data: np.ndarray, levels: list = None, colours: list = None,
           contour: bool = False, fill: bool = False):
        """
        Function to draw T-x diagram.

        :param temperature: :class:`np.ndarray` of temperatures
        :param Xi: :class:`np.ndarray` of compositions
        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param colours: Colours for cmap
        :type colours: list[str]
        :param contour: Switch for contour plot
        :type contour: bool
        :param fill: Switch for filled contour plot
        :type fill: bool
        """
        self.ax_labels = ["x", "Temperature, K"]

        if contour:
            return self.draw_contourmap(x=Xi, y=temperature, data=data, levels=levels, fill=fill)
        else:
            return self.draw_surf(x=Xi, y=temperature, data=data, colours=colours, levels=levels)

    def PT(self, pressure: np.ndarray, temperature: np.ndarray, data: np.ndarray, levels: list = None,
           colours: list = None, contour: bool = False, fill: bool = False):
        """
        Function to draw P-T diagram.

        :param pressure: :class:`np.ndarray` of pressures
        :param temperature: :class:`np.ndarray` of temperatures
        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param colours: Colours for cmap
        :type colours: list[str]
        :param contour: Switch for contour plot
        :type contour: bool
        :param fill: Switch for filled contour plot
        :type fill: bool
        """
        self.ax_labels = ["Temperature, K", "Pressure, bar"]

        if contour:
            return self.draw_contourmap(x=temperature, y=pressure, data=data, levels=levels, fill=fill)
        else:
            return self.draw_surf(x=temperature, y=pressure, data=data, colours=colours, levels=levels)


class NCompDiagram(Diagram):
    """
    This is a base class for construction of N-component diagrams.
    """

    def __init__(self, nc: int, dz: float, min_z: list = None, max_z: list = None,
                 nrows: int = 1, ncols: int = 1, figsize: tuple = (10, 10)):
        """
        The constructor will find the set of physical compositions.

        :param nc: Number of components
        :type nc: int
        :param dz: Mesh size of compositions
        :type dz: float
        :param min_z: Minimum composition of each component (i = 1,...,nc-1), optional
        :type min_z: list[float]
        :param max_z: Maximum composition of each component (i = 1,...,nc-1), optional
        :type max_z: list[float]
        :param nrows: Number of rows for subplots
        :type nrows: int
        :param ncols: Number of columns for subplots
        :type ncols: int
        :param figsize: Size of figure object
        :type figsize: tuple[float]
        """
        super().__init__(nrows, ncols, figsize)

        min_z = min_z if min_z is not None else [dz for i in range(nc - 1)]
        max_z = max_z if max_z is not None else [1. for i in range(nc - 1)]
        n_points = [int(np.ceil((max_z[i] - min_z[i]) / dz)) - (nc - 2) for i in range(nc - 1)]

        comp_bound = np.array(
            [[min_z[i] if min_z[i] > dz else dz, max_z[i] if max_z[i] < 1 else 1 - dz * (nc - 1)] for i in
             range(nc - 1)])
        comp_vec = [np.linspace(comp_bound[i, 0], comp_bound[i, 1], n_points[i]) for i in range(nc - 1)]
        composition = np.zeros((np.prod(n_points), nc))

        if nc == 2:
            composition[:, 0] = comp_vec[0][:]
        elif nc == 3:
            for ii in range(n_points[0]):
                composition[ii * n_points[1]:(ii + 1) * n_points[1], 0] = comp_vec[0][ii]
                for jj in range(n_points[1]):
                    composition[ii * n_points[1] + jj, 1] = comp_vec[1][jj]
        elif nc == 4:
            for ii in range(n_points[0]):
                composition[ii * n_points[1] * n_points[2]:(ii + 1) * n_points[1] * n_points[2], 0] = comp_vec[0][ii]
                for jj in range(n_points[1]):
                    composition[
                    ii * n_points[1] * n_points[2] + jj * n_points[2]:ii * n_points[1] * n_points[2] + (jj + 1) *
                                                                      n_points[2], 1] = comp_vec[1][jj]
                    for kk in range(n_points[2]):
                        composition[ii * n_points[1] * n_points[2] + jj * n_points[2] + kk, 2] = comp_vec[2][kk]

        composition[:, -1] = 1. - np.sum(composition, 1)
        self.comp_physical = composition[(composition[:, -1] >= dz - 1e-10) *
                                         (composition[:, -1] <= 1 - (nc - 1) * dz + 1e-10)]


class BinaryDiagram(NCompDiagram):
    """
    This class can construct binary diagrams.
    """

    def __init__(self, dz: float, min_z: list = None, max_z: list = None,
                 nrows: int = 1, ncols: int = 1, figsize: tuple = (10, 10)):
        """
        The constructor will find the set of physical compositions for nc=2.

        :param dz: Mesh size of compositions
        :type dz: float
        :param min_z: Minimum composition of each component (i = 1,...,nc-1), optional
        :type min_z: list[float]
        :param max_z: Maximum composition of each component (i = 1,...,nc-1), optional
        :type max_z: list[float]
        :param nrows: Number of rows for subplots
        :type nrows: int
        :param ncols: Number of columns for subplots
        :type ncols: int
        :param figsize: Size of figure object
        :type figsize: tuple[float]
        """
        super().__init__(nc=2, dz=dz, min_z=min_z, max_z=max_z, nrows=nrows, ncols=ncols, figsize=figsize)

        self.x0 = self.comp_physical[:, 0]
        self.xlim = [self.x0[0], self.x0[-1]]

    def draw_line(self, data: np.ndarray, color: str = None, label: str = None):
        """
        Function to draw line for binary diagram.

        :param data: :class:`np.ndarray` of data for plotting
        :param color: Line colour
        :type color: str
        :param label: Label for line
        :type label: str
        """
        self.ax.plot(self.x0, data, color=color, label=label)

        return


class TernaryDiagram(NCompDiagram):
    """
    This class can construct ternary diagrams.
    """

    def __init__(self, dz: float, min_z: list = None, max_z: list = None,
                 nrows: int = 1, ncols: int = 1, figsize: tuple = (10, 10)):
        """
        The constructor will find the set of physical compositions for nc=3.

        :param dz: Mesh size of compositions
        :type dz: float
        :param min_z: Minimum composition of each component (i = 1,...,nc-1), optional
        :type min_z: list[float]
        :param max_z: Maximum composition of each component (i = 1,...,nc-1), optional
        :type max_z: list[float]
        :param nrows: Number of rows for subplots
        :type nrows: int
        :param ncols: Number of columns for subplots
        :type ncols: int
        :param figsize: Size of figure object
        :type figsize: tuple[float]
        """
        super().__init__(nc=3, dz=dz, min_z=min_z, max_z=max_z, nrows=nrows, ncols=ncols, figsize=figsize)

        # barycentric coords: (a,b,c)
        self.a = self.comp_physical[:, 0]
        self.b = self.comp_physical[:, 1]
        self.c = self.comp_physical[:, 2]
        self.n_data_points = self.a.shape[0]

    def triangulation(self):
        """
        Function to construct triangular grid and axis.

        :param ax: Axis objects
        :type ax: :class:`matplotlib.pyplot.Axes`

        :returns: Triangular grid and Axes
        :rtype: :class:`matplotlib.tri.Triangulation`, :class:`matplotlib.pyplot.Axes`
        """
        # plot triangle
        z = np.array([[0, 0], [1, 0], [0, 1], [0, 0]])
        x = 0.5 - z[:, 0] * np.cos(np.pi / 3) + z[:, 1] / 2
        y = 0.866 - z[:, 0] * np.sin(np.pi / 3) - z[:, 1] / np.tan(np.pi / 6) / 2
        self.ax.plot(x, y, 'k', 'linewidth', 1.5)

        # create the grid
        corners = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) * 0.5]])
        triangle = tri.Triangulation(corners[:, 0], corners[:, 1])

        # refining the grid
        # refiner = tri.UniformTriRefiner(triangle)
        # trimesh = refiner.refine_triangulation(subdiv=2)

        # plotting the mesh
        self.ax.triplot(triangle, color='navajowhite', linestyle='--', linewidth=0.8)
        # ax.triplot(trimesh, color='navajowhite', linestyle='--', linewidth=0.8)
        self.ax.set_ylim([0, 1])
        self.ax.axis('off')

        # translate the data to cartesian corrds
        self.x = 0.5 * (2. * self.b + self.c) / (self.a + self.b + self.c)
        self.y = 0.5 * np.sqrt(3) * self.c / (self.a + self.b + self.c)

        # create a triangulation out of these points
        T = tri.Triangulation(self.x, self.y)

        # plot the contour
        self.ax.plot([0, 1, 0.5, 0], [0, 0, np.sqrt(3) / 2, 0], linewidth=1)
        # fig.rc('font', size=12)

        return T

    def draw_surf(self, data: np.ndarray, levels: list = None, colours: list = None):
        """
        Function to draw 2D pcolormesh.

        :param data: :class:`np.ndarray` of data for plotting
        :param levels: Levels for legend
        :type levels: list
        :param colours: Colours for ListedColormap
        :type colours: list[str]
        """
        if colours is None:
            cmap = 'RdBu'
            # cmap = plt.get_cmap('RdBu', np.max(data) - np.min(data) + 1)
        elif isinstance(colours, list):
            cmap = colors.ListedColormap(colours)
        else:
            cmap = colours

        vmin = np.amin(data) * 0.999  # -10.1
        vmax = np.amax(data) * 1.001  # 10.1
        levels = np.linspace(vmin, vmax, 101) if levels is None else levels

        # Create triangular
        T = self.triangulation()

        # plot the contour
        self.im = self.ax.tricontourf(self.x, self.y, T.triangles, data, levels=levels)

        return

    def draw_contourmap(self, data: np.ndarray, n_levels: int = None, colours: list = None, fill: bool = None):
        """
        Function to draw ternary contour plot.

        :param data: :class:`np.ndarray` of data for plotting
        :param n_levels: Number of contour levels
        :type n_levels: int
        :param colours: Colourmap
        :type colours: list or :class:`matplotlib.colors.Colormap`
        :param fill: Switch for filled contour plot
        :type fill: bool
        """
        if colours is None:
            cmap = 'RdBu'
            # cmap = plt.get_cmap('RdBu', np.max(data) - np.min(data) + 1)
        elif isinstance(colours, list):
            cmap = colors.ListedColormap(colours)
        else:
            cmap = colours

        vmin = np.amin(data) * 0.999  # -10.1
        vmax = np.amax(data) * 1.001  # 10.1
        levels = np.linspace(vmin, vmax, n_levels) if n_levels is not None else np.linspace(vmin, vmax, 101)

        # Create triangular
        T = self.triangulation()

        # plot the contour
        if fill:
            self.im = self.ax.tricontourf(self.x, self.y, T.triangles, data, levels=levels)
        else:
            self.im = self.ax.tricontour(self.x, self.y, T.triangles, data, levels=levels)

        return

    def draw_line(self, compositions: list, color: str = None, linestyle: str = 'solid'):
        """
        Function to draw line in ternary plot.

        :param compositions: Compositions of end points [[x0, y0, z0], [x1, y1, z1], ...]
        :type compositions: list[list[float]]
        :param color: Line colour, optional
        :type color: str
        :param linestyle: Linestyle, optional
        :type linestyle: str
        """
        # Calculate mole fractions
        compositions = np.array(compositions)
        compositions = np.array([comp / np.sum(comp) for comp in compositions])

        # translate the data to cords
        x = (1 - compositions[:, 0]) * np.cos(np.pi / 3) + compositions[:, 1] / 2
        y = (1 - compositions[:, 0]) * np.sin(np.pi / 3) - compositions[:, 1] / np.tan(np.pi / 6) / 2
        self.ax.plot(x, y, color=color, linestyle=linestyle)

        return

    def draw_point(self, compositions: list, color: str = None, marker: str = None):
        """
        Function to draw point in ternary plot.

        :param compositions: Compositions of points [[x0, y0, z0], [x1, y1, z1], ...]
        :type compositions: list[list[float]]
        :param color: Point colour, optional
        :type color: str
        :param marker: Point marker, optional
        :type marker: str
        """
        # Calculate mole fractions
        compositions = np.array(compositions)
        compositions = np.array([comp / np.sum(comp) for comp in compositions])

        # translate the data to cords
        x = (1 - compositions[:, 0]) * np.cos(np.pi / 3) + compositions[:, 1] / 2
        y = (1 - compositions[:, 0]) * np.sin(np.pi / 3) - compositions[:, 1] / np.tan(np.pi / 6) / 2
        self.ax.scatter(x, y, color=color, marker=marker)

        return

    def add_attributes(self, title: str = None, ax_labels: list = None, legend: bool = False, colorbar: bool = False,
                       corner_labels: list = None):
        """
        Function to add attributes to ternary diagram.

        :param fig: :class:`matplotlib.pyplot.Figure` object
        :param ax: :class:`matplotlib.pyplot.Axes` objects
        :param title: Figure title
        :type title: str
        :param ax_labels: Axes labels
        :type ax_labels: list[str]
        :param legend: Switch to add legend for lines/points
        :type legend: bool
        :param colorbar: Switch to add colorbar
        :type colorbar: bool
        """
        Diagram.add_attributes(self, title=title, legend=legend)

        # colorbar
        if colorbar:
            cax = plt.axes([0.75, 0.55, 0.055, 0.3])
            self.im.colorbar(cax=cax, format='%.3f', label='')

        # labels at corner points
        if corner_labels:
            self.fig.text(0.08, 0.1, '$' + corner_labels[0] + '$', fontsize=20, color='black')
            self.fig.text(0.91, 0.1, '$' + corner_labels[1] + '$', fontsize=20, color='black')
            self.fig.text(0.5, 0.8, '$' + corner_labels[2] + '$', fontsize=20, color='black')

        return


class QuaternaryDiagram(NCompDiagram):
    """
    This class can construct quaternary diagrams.
    """

    def __init__(self, dz, min_z: list = None, max_z: list = None,
                 nrows: int = 1, ncols: int = 1, figsize: tuple = (10, 10)):
        """
        The constructor will find the set of physical compositions for nc=4.

        :param dz: Mesh size of compositions
        :type dz: float
        :param min_z: Minimum composition of each component (i = 1,...,nc-1), optional
        :type min_z: list[float]
        :param max_z: Maximum composition of each component (i = 1,...,nc-1), optional
        :type max_z: list[float]
        :param nrows: Number of rows for subplots
        :type nrows: int
        :param ncols: Number of columns for subplots
        :type ncols: int
        :param figsize: Size of figure object
        :type figsize: tuple[float]
        """
        super().__init__(nc=4, dz=dz, min_z=min_z, max_z=max_z, nrows=nrows, ncols=ncols, figsize=figsize)

        # barycentric coords: (a,b,c)
        self.a = self.comp_physical[:, 0]
        self.b = self.comp_physical[:, 1]
        self.c = self.comp_physical[:, 2]
        self.d = self.comp_physical[:, 3]
        self.n_data_points = self.a.shape[0]

    def quaternary(self):
        return
