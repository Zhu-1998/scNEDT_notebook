|PyPI| |PyPIDownloads| |Docs|

scNEDT - single-cell NonEquilibrium Dynamics and Thermodynamics
===============================================================

.. image:: https://github.com/Zhu-1998/scNEDT_notebook/blob/main/docs/source/_static/logo.png
   :width: 300px
   :align: left


**scNEDT** is a scalable toolkit for NonEquilibrium Dynamical and Thermodynamical analysis in single cells, which
enables the recovery of the underlying driving force and physical mechanisms of cell functions. scNEDT collects two different
methods for quantifying the nonequilibrium dynamics and thermodynamics by single-cell dynamic 
force field reconstruction or master equation :cite:p:`Fang2020`.

scNEDT's key applications
^^^^^^^^^^^^^^^^^^^^^^^^^
- Quantify nonequilibrium potential landscape and flux to study cellular dynamics driving force.
- Map the optimal path and identify the transition state and driver genes of cell fate decisions.
- Infer nonequilibrium thermodynamics of cell function, e.g., entropy, energy production rate, heat disspation rate, chemical potential.
- Dynamic loop-flux decomposition and loop-flux drives cell development.
- Early warning indicators for diseases using time-resolved single-cell transcriptomics, e.g., cancer initation, progression, EMT.


Citing scNEDT
^^^^^^^^^^^^^

If you include or rely on scNEDT when publishing research, please adhere to the
following citation guide:

https://github.com/Zhu-1998/scNEDT

Support
^^^^^^^
If you find a bug of scNEDT, please submit an
`issue <https://github.com/Zhu-1998/scNEDT/issues/new/choose>`_.
And if you have a question or would like to start a new discussion, please join the 
`GitHub discussions <https://github.com/Zhu-1998/scNEDT/discussions>`_.
Your help to improve scNEDT is highly appreciated.


.. toctree::
   :caption: Main
   :maxdepth: 1
   :hidden:

   about
   installation
   api
   release_notes
   references

.. toctree::
   :caption: CONTINUOUS DYNAMICS
   :maxdepth: 1
   :hidden:

   notebooks/Driving_forces
   notebooks/Optimal_path
   notebooks/Nonequilibrium_thermodynamics
   notebooks/Nonequilibrium_dynamics

.. toctree::
   :caption: DISCRETE DYNAMICS
   :maxdepth: 1
   :hidden:

   notebooks/Potential
   notebooks/Thermodynamics
   notebooks/Loop_flux_decomposition

.. toctree::
   :caption: EARLY WARNING INDICATORS
   :maxdepth: 1
   :hidden:

   notebooks/Dynamic_flux
   notebooks/Thermodynamical_disspation
   notebooks/Critical_slow_down
   notebooks/Time_reversal_symmetry_breaking


.. |PyPI| image:: https://img.shields.io/pypi/v/scnedt.svg
   :target: https://pypi.org/project/scnedt

.. |PyPIDownloads| image:: https://pepy.tech/badge/scnedt
   :target: https://pepy.tech/project/scnedt

.. |Docs| image:: https://readthedocs.org/projects/scnedt/badge/?version=latest
   :target: https://scnedt.readthedocs.io

.. _Scanpy: https://scanpy.readthedocs.io

.. |br| raw:: html

  <br/>

.. |dim| raw:: html

   <span class="__dimensions_badge_embed__" data-id="pub.1129830274" data-style="small_rectangle"></span>
   <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
