About scNEDT
------------

scNEDT is a scalable toolkit designed for NonEquilibrium Dynamical and Thermodynamical analysis in single cells. 
Its core purpose is to recover the underlying driving force and physical mechanisms that govern cell functions. 
By leveraging this framework, researchers can gain deeper insights into the nonequilibrium nature of cellular processes, 
helping to quantify how cells dissipate energy and maintain their functional states.

Quantification of Nonequilibrium Dynamics and Thermodynamics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
scNEDT includes two distinct methods to achieve this:

- **Single-cell dynamic force field reconstruction**: This method enables the direct reconstruction of the forces driving cellular dynamics. By analyzing single-cell trajectories or behaviors over time, the toolkit can infer the force fields governing these processes. These forces often emerge from molecular interactions and signaling events.
- **Master equation-based approach**: The master equation formalism is used to model stochastic processes in systems with discrete states. It describes the probability distribution of states in the system and how this distribution evolves over time, capturing transitions between different cell states (e.g., different phenotypes or functional states).
