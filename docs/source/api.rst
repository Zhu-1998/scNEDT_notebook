.. automodule:: scnedt

API
===

Import scNEDT as::

   import scnedt as scn




Forcefield (ff)
---------------

**Force field topography**

.. autosummary::
   :toctree: .

   ff.force_field
   ff.velocity_field

**Differential geometry**

.. autosummary::
   :toctree: .

   ff.acceleration
   ff.curl
   ff.curvature
   ff.divergence
   ff.jacobian
   ff.speed
   ff.vorticity


Quantifying nonequilibrium driving forces, landscape-flux (lf)
--------------------------------------------------------------

.. autosummary::
   :toctree: .

   lf.curl_flux
   lf.gradient_force
   lf.mean_force


Master equation (me)
--------------------

.. autosummary::
   :toctree: .

   me.master_equation
   me.loop_flux
   me.net_flux



Tools (tl)
----------

**State steady probility and potential landscape**

.. autosummary::
   :toctree: .

   tl.landscape

**Fixed point**

.. autosummary::
   :toctree: .

   tl.fixed_points


**Differential geometry**

.. autosummary::
   :toctree: .

   tl.acceleration
   tl.curl
   tl.curvature
   tl.divergence
   tl.jacobian
   tl.speed
   tl.vorticity


**Least action path**

.. autosummary::
   :toctree: .

   tl.LAP


Thermodynamics (td)
-------------------

.. autosummary::
   :toctree: .

   td.Entropy
   td.EPR_ff
   td.EPR_ms
   td.HDR_ff
   td.HDR_ms
   td.chemical_potential


Dynamics (ds)
-------------

.. autosummary::
   :toctree: .

   ds.MFPT
   ds.auto_corr
   ds.cross_corr
   ds.CSD
   ds.delta_cc



Plotting (pl)
-------------

**Plot scatter**

.. autosummary::
   :toctree: .

   pl.scatter
   pl.scatters



**Plot velocity**

.. autosummary::
   :toctree: .

   pl.velocity_stream


**Plot force field**

.. autosummary::
   :toctree: .

   pl.topography
   pl.mean_force_stream
   pl.mean_force_arrow
   pl.gradient_force_stream
   pl.gradient_force_arrow
   pl.curl_flux_stream
   pl.curl_flux_arrow


**Landscape plot**

.. autosummary::
   :toctree: .

   pl.landscape_2D
   pl.landscape_3D
   pl.potential_3D
   

**Least action path**

.. autosummary::
   :toctree: .

   pl.lap
   pl.lap_2Dlandscape
   pl.lap_lap_3Dlandscape
   

**Matrix**

.. autosummary::
   :toctree: .

   pl.matrix_heatmap
   pl.connectivity_graph

**Loop flux**

.. autosummary::
   :toctree: .

   pl.loop_flux

**Further plotting**

.. autosummary::
   :toctree: .

   pl.heatmap
   pl.mfpt
   pl.auto_corr
   pl.cross_corr
   pl.delta_cc
   pl.csd


