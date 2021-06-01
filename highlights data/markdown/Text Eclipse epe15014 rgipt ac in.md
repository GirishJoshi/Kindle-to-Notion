

In reservoir simulators the objective is much the same – to simulate the exploitation of a real reservoir without the costs of real life trial and error, e.g. to test different productions scenarios to find an optimal one before the reservoir is actually put on production.

The description of the reservoir and the boundary conditions for the equations for flow in a porous rock are known only with a great deal of uncertainty.

Primarily, the pore system itself and the flow in this system happens on a detail level that is impossible to describe or model – and if it were possible the resulting problem would be too large to solve on present-day computers anyway. In addition to that, the detail structure of the pore system will obviously be unknown. So the problems we look at are a result of.

This is, because even if there may be uncertainties tied to simulated results, the simulations reveal invaluable information about the reservoir flow, and not the least, can point to areas which need closer investigation or can represent elements of risk to the production scenarios.

Evaluate the quality of the input data.

Transform the input data to a form suitable for simulation.

Identify which parts of the data are most sensitive to uncertainty.

Identify necessary additional data acquisition.

Identify key data which may directly influence choice of operations plans, and uncertainty tied to these.

Perform a suite of reservoir simulations.

Evaluate quality of results from the simulations, uncertainties, areas of robustness.

Utilize available field production data to tune simulations.

Point to potential future problems / solutions, suggest production plans.

Eclipse, by Geoquest / Schlumberger,.

The objective of these lecture notes is thus to enable the user to understand the required input data to a reservoir simulator, convert the input issues to Eclipse format and run simulations with Eclipse, for not-too-complex problems.

Decisions based on the simulations are the goal, not the simulations.

It is the use of the simulator that is important, not the technicalities.

One of the important tasks for a user of a reservoir simulator is to evaluate the quality of simulated results. Are the results “as expected”? – Do the results appear trustworthy?.

It is the author’s opinion and experience that input data will generally be of higher quality, potential simulation errors will be quicker identified, and result evaluation will be more robust if the user has some knowledge of how the input data is handled by the simulator.

It is therefore necessary to subdivide the continuous reservoir into a finite number of discrete elements, and also to define time development in a discrete sense.

The subdivision of the reservoir into finite volume elements or cells is denoted a discretisation of the reservoir, and the set of elements is called the reservoir grid.

The grid is then uniquely defined by the size of each cube, and the number of cubes in each of the major directions, X, Y, Z.

I, J, K are used for indices in X, Y, Z – directions, and the ordering is defined as in “normal reading order”, i.e. I runs from left to right, J runs from top of a page to bottom, and K runs from page to page. In a grid oriented along standard geographical axes, I would increase from west to east, J would increase from north to south, and K downwards.

Is to allow for DX to be dependent on the I-index, and DY to be dependent on the J-index.

We generally try to honour the depth variation of the units in the grid.

Although permeability is a tensor variable, Eclipse only allows for the diagonal elements Kxx, Kyy, and Kzz, called PERMX, PERMY, and PERMZ.

The simplest and most used assumption is constant compressibility.

The initial reservoir state is defined by the pressure and saturations in each grid cell at the start of the simulation.

Assumption that the reservoir fluids are in equilibrium at no-flow conditions.

We then only need supply the depths of the oil-water and gas-oil contacts, and the fluid pressures at a reference depth. The simulator can then calculate the necessary state from fluid weight versus depth gradients.

Describe the well positions, at which depths they are open to the reservoir, and the production or injection rates.

During the field’s life time, wells will be added or closed, well rates will be changed, and operating constraints may be added or removed. All such events are handled by defining a series of milestones, dates at which operating conditions may change.

All data needed by Eclipse is collected in an input data file, which is an ordinary text file.

The keyword data is always terminated by a slash (‘/’).

An Eclipse data file is comprised of eight sections headed by a section header.

RUNSPEC (required) Run specifications. Includes a description of the run, such as grid size, table sizes, number of wells, which phases to include an so forth. GRID (required) Defines the grid dimensions and shape, including petrophysics (porosity, permeability, net-togross). EDIT (optional) User-defined changes to the grid data which are applied after Eclipse has processed them, can be defined in this section. The EDIT section will not be covered in these notes. PROPS (required) Fluid and rock properties (relative permeabilities, PVT tables, ...) REGIONS (optional) User defined report regions, or e.g. regions where different rel.-perm. curves apply can be defined in this section. SOLUTION (required) Equilibration data (description of how the model is to be initialised). SUMMARY (optional) Results output is primarily of two types: 1) Scalar data as a function of time (e.g. average field pressure) 2) Data with one value pr. grid cell (e.g. oil saturation). These are only output at chosen times. This section is used to define output of the first kind, by specifying which data items to write to report files. SCHEDULE (required) Well definitions, description of operating schedule, convergence control, control of output of the second kind described above.

Any line in an Eclipse input file that starts with two dashes (--) is treated as a comment.

(Note that the two dashes must be in column 1 and 2, no leading blanks.).

Note that it is allowed to put a comment after the terminating slash.

It is typically generated by an external program, like e.g. IRAP RMS or FloGrid, not input manually.

We assume that porosity is constant in each layer.

PORO 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.24 0.25 0.25 0.25 / is equivalent to PORO 8*0.23 0.24 3*0.25 / Note that there must not be any blanks on any side of the asterisk (star).

Eclipse has defined default values for many values, and if we on input set these items to default, Eclipse will use the defined default values instead.

A default value is specified by “1*”, and can be repeated as above, with n* (e.g. to specify that the next three items shall be defaulted use 3*).

(The main reason for using relative addressing is that we then can move an entire project to a new parent folder without having to change all the INCLUDEs in the data files.).

What are they?.

Unified files.

Eclipse is written in FORTRAN,.

Eclipse is written in FORTRAN, and does not use dynamic memory allocation.

Eclipse must know how many wells to allocate memory for, and how much memory is needed for each well.

Firstly the grid is a set of finite volume cells which approximates the reservoir volume including internal characteristics. Secondly the grid is a device for solving the reservoir flow equations in a numerical fashion.

Compromise between actual reservoir shape, numeric accuracy and affordable computing time is a science in itself, which cannot be covered in this context.

DX and DY are of comparable magnitude, and DZ much smaller.

The major reason that XY-cartesian grids are not more or less exclusively used is the existence of faults in the reservoir.

One alternative solution which is growing in popularity, is to use unstructured grids. By allowing for cells with any number of faces, any geometry can be modelled, and at the same time keeping the total number of cells at a manageable level.

A structured grid obeying the coordinate line restriction was originally called a corner point grid by the Eclipse development team. The Eclipse grid format is now a de facto industry standard, and corner point grids are used in a much wider context.

The constraint defined by Eclipse is then that cell corners N1A, N1B,..., N4A, N4B lie on the coordinate line for all layers K.

The constraint defined by Eclipse is then that cell corners N1A, N1B,..., N4A, N4B lie on the coordinate line for all layers K. A way of looking at this is to envisage the coordinate line as a straw, and the corner nodes as beads on this straw. The beads can move up and down on the straw, but are restricted to stay on the straw, which by definition cannot be bended – coordinate lines must be straight lines.

Most or all complex grids for real field simulations are constructed with dedicated software like FloGrid or IRAP RMS.

Then flow in the x-direction will be completely stopped by the slab, such that the effective permeability across the cube in the x-direction is zero, which is also what we would get if we compute the harmonic average.

Another source for inactive cells is the minimum pore volume option. Cells with very small pore volume will contribute insignificantly to flow or production, but exactly because they have a pore volume which is very different from typical values they can have a negative effect on the numerical solution, and total computing time can become (unacceptable) large. For this reason it is possible and advisable to define a minimum pore volume value such that cells with smaller pore volume than this value will be flagged as inactive. For Eclipse, see keywords MINPV or MINPVV.

An inactive cell is a cell that does not contribute to fluid volumes or flow in the reservoir. By default, the simulator will flag any cell with vanishing pore volume as inactive. In addition, the user may define active cells explicitly, by the keyword ACTNUM, where all cells are listed, the active ones as “1”, inactive as “0”.

Important Section.

Permeability is a measure for conductance, and its inverse is a measure for resistance. If we draw the comparison to electrical resistance or conductance, it is evident that we never speak of “resistance in a point”. Resistance or conductance is a property that only has meaning if referred to as “between two points”, i.e. conductance and resistance is a flow property. In the same manner, it is meaningless to speak of “permeability in a point”. If we regard the grid cell as a volume, we could interpret permeability as the flow property across the cell. However, viewing the cell as a volume is solely a convenient visualisation means. By the manner the simulator solves the flow equations the grid is a set of points, and all property values are to be understood as the values in the points. And obviously nothing can vary “in a point”. (By this way of looking at the grid we are less tempted to think that it is possible to model variations within a grid cell volume. If the point of interest is really a point it is evident that no variation can be possible.) The bottom line is that the permeabilities of interest should really be measures for conductivity between different grid points.

Transmissibility.


