

With experience, it becomes painfully obvious— many reservoir engineering estimates, plans, and schemes have fundamental ﬂaws. In some cases, it is possible to identify a wrong assumption as the central cause of the problem. Unfortunately, this is not the norm. Most often, it will be attributed to a combination of things; some.

Screening Most reservoir engineering textbooks do not have a section dealing with how to screen the input data. There are no examples of bad data. The point is that doing a reservoir simulation probably will put most practicing engineers into new territory.

On a philosophical note, the essence of Buddhism is ignorance is our sole enemy. In simplistic terms, it replaces sin. This general concept is sometimes coined lifelong learning.

As a reservoir matures and more.

At the other extreme, some petroleum engineers are convinced reservoir engineering analysis is so theoretical as to be of no practical application. Do not believe this. Most senior engineering managers, vice presidents, and quite a few presidents have a reservoir engineering background.

One of the most important skills is the ability to recognize good and bad input data.

One of the most important skills is the ability to recognize good and bad input data. If engineers have operational experience, they have an advantage.

Only fools learn from their mistakes, I prefer to learn from others’ mistakes.

This book has been prepared in a conversational style. In many cases, there are a number of observations the author has made and not attempted to prove scientiﬁcally. In the author’s opinion, a signiﬁcant aspect of reservoir engineering is the thought process or approach. One of the objectives is to prepare reports to outline this thinking. This has been recognized lately and is often called an expert system, which is coincidentally associated with artiﬁcial intelligence (AI). This indicates the thought process has been recognized as a signiﬁcant determinant of success. Many engineers.

This book has been prepared in a conversational style. In many cases, there are a number of observations the author has made and not attempted to prove scientiﬁcally. In the author’s opinion, a signiﬁcant aspect of reservoir engineering is the thought process or approach. One of the objectives is to prepare reports to outline this thinking. This has been recognized lately and is often called an expert system, which is coincidentally associated with artiﬁcial intelligence (AI). This indicates the thought process has.

This book has been prepared in a conversational style. In many cases, there are a number of observations the author has made and not attempted to prove scientiﬁcally. In the author’s opinion, a signiﬁcant aspect of reservoir engineering is the thought process or approach. One of the objectives is to prepare reports to outline this thinking. This has been recognized lately and is often called an expert system, which is coincidentally associated with artiﬁcial intelligence (AI). This indicates the thought process has been recognized as a signiﬁcant determinant of success.

The input to the simulator is tuned.The model is run with the historical base product production speciﬁed—usually oil. The idea is to match GORs, water cuts, and pressures predicted by the model to actual performance.This part of the study is usually the most timeconsuming, normally averaging one-third of total study time. The permeability × height (kh) or bottomhole pressure (bhp) of the wells is then adjusted so base product production matches actual ﬁeld performance.

At the end of the history-matching phase,the results are stored in a special restart ﬁle.With.

At the end of the history-matching phase,the results are stored in a special restart ﬁle.With this,it is possible for the reservoir simulation to be continued without rerunning the problem through the history match. After completing the history match, various predictions are made using different production, well, and injection scenarios.The results can.

Layering calculations include those of Stiles and Dykstra-Parsons.

Grid-block water saturations are calculated based on capillary pressure data.The.

In order to make predictions, the kh, or bottomhole pressure, of all wells must be adjusted to match actual production performance.This involves a series of trial and error runs to obtain the correct values.

Stage.At the end of the tuning phase the model is usually terminated with a restart.This input data ﬁle contains all of the information necessary to continue a simulation at a later time. Several different production scenarios or alternatives are run from the same timestep and compared.With different runs, various injector patterns, changes in rates, and producer.

The assumptions on which a simulation is based should be outlined. Simulation also generates an enormous amount of paper output. It takes considerable time and ingenuity to reduce this data to an understandable form from a commonsense perspective.

First, almost all reservoir data is in the public domain.

The author has spent a great deal of time in Western Canada and has experience on reservoirs in Peru, Bangladesh, India, Australia, Indonesia, and the Former Soviet Union (FSU) as well. The.

A number of factors, such as basin maturity and geological controls, were considered in preparing this ﬁgure; however, it is logical to extrapolate exploration success with increased information. This was—and is—the purpose of making the data public.

Correctly applied, reservoir simulation can be a powerful tool. It is extremely dangerous if applied incorrectly. It is a similar to riding a high-performance sailboat in a big wind. If you don’t respect it, you will likely get hurt. If you fear it (or are overawed by it), you will not be able to control it, and you will end up in the drink. You can never take your eyes off what is happening and where you are going, because something unpredictable will happen when you do. It takes time and practice to become good. Sailing is not for everyone but is addictive to others. Each study will be a variation on a common theme. However, the emphasis on the various components in different studies will change with individual reservoirs and the stage of the reservoir in its production life cycle.

The author participated in a course taught by Dr. A. Settari, which required a simulator be built as a class project. This problem set had a reputation for being long, involved, and difﬁcult.

Reading pages of differential equations and matrices is not the same as actually programming a simulator.

The development of the partial differential equations is the same for a reservoir simulator as for pressure transient analysis.

First, a description of the behavior of the ﬂuids at different pressures is required—an equation of state; and, second, an interblock transport relation is required.

For gas, the real gas law is used. • The liquid phase has dissolved gas, which is a linear function of pressure (black oil). • Water is characterized as a liquid of low compressibility, which is a linear function of pressure.

The intrinsic property of the rock is termed permeability. Note there is a breakdown at high Reynolds numbers.

Directions. This directional change in permeability is not directly programmed into reservoir simulators, as.

This level of error is considered tolerable in the majority of cases.

There are certain cases where this error is not acceptable. Probably the most common is in thermal simulation where adverse mobility ratios (i.e., much greater than one) exist in displacements. Gas (steam) displacement of viscous oil—i.e., heavy oil—is a classic example. The converse, where oil displaces gas, does not cause problems.

This case, the differential equations are formed differently: ﬂow is allowed diagonally between grid blocks.

The solution to this equation is not going to be solved exactly. Approximate solutions are going to be developed at certain ﬁxed points in space and, as the simulator marches through certain ﬁxed points, in time. Thus, two discretizations occur, one in space and the other in time.

The solution to this equation is not going to be solved exactly. Approximate solutions are going to be developed at certain ﬁxed points in space and, as the simulator marches through certain ﬁxed points, in time. Thus, two discretizations occur, one in space and the other in time. The discrete points in space are arbitrarily chosen using a grid.

One is called a block-centered grid and the other a.

One is called a block-centered grid and the other a pointcentered grid. The boundary conditions for these two types of grids are different; however, all of the commercial simulators use block-centered grids.

Time discretization is accomplished with timesteps. These are also arbitrarily chosen.

The accuracy of the solution.

Smaller grid blocks and shorter timesteps provide more accurate solutions.

In order to handle the large volumes of computational data, matrices are used to solve these problems.

The solution at time n + 1 is on the left side. On the far left-hand side are all of the spatial terms, which are made up of permeability and grid-block dimensions. The next term, on the right-hand side, represents the length of the timestep and the previous solution (pressures and grid-block production rates), which completes the information necessary to project the solution at the end of the timestep.

The initial solution or pressures must be set to start the simulation and a series of grid-block values are obtained from the simulator at discrete points in time.

Regular grid, the error is proportional to the spacing squared.

Regular grid, the error is proportional to the spacing squared. For an irregular grid, the error is directly related to the spacing.

Is not possible to determine the absolute level of error from this technique, only how it varies with spacing. Therefore, to determine the absolute level of error, it is necessary to compare a computer simulation with an analytical solution.

These analytical solutions are only available for certain geometries, and, as a result, the accuracy of most real simulations cannot be determined absolutely.

However, multiple runs made with different grid spacing can be compared to each other, which indicates convergence to a consistent solution is rapid and changes in solutions are of.

However, multiple runs made with different grid spacing can be compared to each other, which indicates convergence to a consistent solution is rapid and changes in solutions are of a small magnitude. This is called a grid sensitivity.

Therefore, it is practical to test the accuracy of a grid using multiple simulation runs. These sensitivities need not be performed on the entire grid. It is generally sufﬁ- cient to make a grid for a small group of wells, which feature the important mechanisms in the reservoir. This allows detailed (small dimension) grid blocks to be explored with realistic simulation execution.

Turbulent ﬂow is described by the Forcheimer equation,.

The base differential equations for pressure transient analysis and reservoir simulation.

The base differential equations for pressure transient analysis and reservoir simulation are the same, although in different coordinate forms: ∂ 2 p ∂ c = p φµ ∂ x 2 ∂ t k ∂ 2 p 1 ∂ p ϕµ c ∂ p 2 + = ∂ rr ∂ r k ∂ t (2.7) (2.8) 2 0 < It is natural to ask is why reservoir simulators are not formulated based on pseudo pressures. The answer is they can. It is even possible to assign a pseudo pressure to oil. The use of pseudo pressure linearizes the 1/µz when dealing with gas. In a reservoir simulation, these factors are all calculated for time.

The use of pseudo pressure linearizes the 1/µz when dealing with gas. In a reservoir simulation, these factors are all calculated.

Implicit versus explicit solutions (formulation/practical knowledge) Using a simplified single-phase example can be solved in two ways. The ﬁrst assumes the pressure gradients in space don’t change much between timesteps.

Implicit versus explicit solutions (formulation/practical knowledge) Using a simplified single-phase example can be solved in two ways. The ﬁrst assumes the pressure gradients in space don’t change much between timesteps. Therefore, the solution at time n + 1 can be estimated from existing values of pressure. This is known as an explicit solution.

After a few experiments, the prediction of the solution at time n + 1 is improved if one takes the solution from time n + 1 and averages it with the original solution at time n, yielding an average effective pressure of (P n+1 + P n )/2 for the iteration. This updated average pressure is then used to reestimate the pressure at time n + 1. The variation in each successive estimate of the solution at time n + 1 is observable using the average pressure across the timestep. The difference between successive iterations can be set at a tolerance deﬁning convergence, and a form of control is introduced. This is known as an implicit solution.

Explicit solutions are based on the solution at the last timestep, and only one leap forward in time is made. Implicit solutions are based on both the previous and current solution and involve multiple estimates of the solution at time n +.

Caused problems in generating the basic formulation for reservoir simulators. The general idea, depicted in Figure 2–12, shows a simpliﬁed onedimensional (1-D) grid. As injected water displaces.

The Buckley-Leverett theory is deﬁcient in one major respect—accounting for capillary pressure.


