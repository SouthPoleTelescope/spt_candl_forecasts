.. raw:: html

   <div style="display: flex; align-items: center;">
     <img src="https://github.com/SouthPoleTelescope/spt_candl_data/blob/main/logos/spt_logo.jpg?raw=true" style="width:35%;"/>
     <img src="https://github.com/SouthPoleTelescope/spt_candl_data/blob/main/logos/blank_padding.png?raw=true" style="width:5%;"/>
     <img src="https://github.com/Lbalkenhol/candl/raw/main/docs/logos/candl_wordmark&symbol_col_RGB.png" style="width:55%;"/>
   </div>
   
   <h1>Official SPT mock likelihoods for forecasts with <tt>candl</tt></h1>

Official SPT mock likelihoods for forecasts with the differentiable CMB likelihood framework `candl <https://github.com/Lbalkenhol/candl>`_.

Download
------------

To download the SPT candl mock likelihoods, simply navigate to where you would like to store the data and then run::

    git clone https://github.com/SouthPoleTelescope/spt_candl_forecasts.git

This will download the relevant data files. Note that you also need to install `candl <https://github.com/Lbalkenhol/candl>`_ in order to run the likelihoods, run ``pip install candl`` or see the repository for more detailed instructions.

Available mock data
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 30

   * - Name
     - Description
     - References

   * - SPT-3G Main T&E
     - | SPT-3G Main field temperature and polarization
       mock likelihood for 5 years of observation
     - Vitrier et al. 2025 (in prep.)

   * - | SPT-3G Summer-a T&E
       | SPT-3G Summer-b T&E
       SPT-3G Summer-c T&E
     - | SPT-3G Summer field temperature and 
       | polarization mock likelihoods for 4 years of 
       observation
     - Vitrier et al. 2025 (in prep.)

   * - | SPT-3G Wide-a T&E
       | SPT-3G Wide-b T&E
       | SPT-3G Wide-c T&E
       | SPT-3G Wide-d T&E
       | SPT-3G Wide-e T&E
       | SPT-3G Wide-f T&E
       | SPT-3G Wide-g T&E
       | SPT-3G Wide-h T&E
       SPT-3G Wide-i T&E
     - | SPT-3G Wide field temperature and polarization 
       mock likelihoods for 1 year of observation
     - Vitrier et al. 2025 (in prep.)
   
   * - SPT-3G Main PP
     - | SPT-3G Main field lensing mock likelihood for 
       5 years of observation
     - Vitrier et al. 2025 (in prep.)
   
   * - | SPT-3G Summer-a PP
       | SPT-3G Summer-b PP
       SPT-3G Summer-c PP
     - | SPT-3G Summer field lensing mock likelihoods 
       for 4 years of observation
     - Vitrier et al. 2025 (in prep.)
   
   * - SPT-3G Wide PP
     - | SPT-3G Wide field lensing mock likelihood for 
       1 year of observation
     - Vitrier et al. 2025 (in prep.)
   
   * - Planck
     - Planck mock likelihood
     - Vitrier et al. 2025 (in prep.)

Additional Info
^^^^^^^^^^^^^^^^^^

In order to forecast cosmological parameter constraints from the full Ext-10k survey, the SPT-3G likelihoods of the different fields have to be combined. The basic combination to start with is in temperature and polarization, combining the 13 fields of the Ext-10k survey (1 Main field, 3 Summer fields, and 9 Wide fields). 

The temperature and polarization nuisance parameter priors are directly provided in the ``.yaml`` file of each field. However, only those of the Main field are de-commented, so that the priors are not counted 13 times. In the case of forecasting constraints from the Wide survey only, the nuisance parameter priors need to be de-commented in one of the Wide fields T&E ``.yaml`` files.

Note that a prior on the optical depth to reionization is also provided in the Main field ``.yaml`` file so that the Ext-10k Fisher matrix can be computed. Be careful not to double count this prior when running Markov Chain Monte Carlo (MCMC).

Getting Started
--------------

We supply files to help you use the SPT mock data with cobaya as well as a tutorial on how to interact with the mock likelihoods.
You can find more help and tutorials in the `candl documentation <http://candl.readthedocs.io>`_.

Notebook
^^^^^^^^^^^^^^

``tutorial_notebooks/SPT3G_Ext10k_TnE_tutorial.ipynb``: this notebook uses the SPT-3G Ext-10k T&E mock likelihoods and shows you how to initialize the likelihoods and compute the Ext-10k T&E Fisher matrix.

Cobaya
^^^^^^^^^^^^^^

You can find a template Cobaya ``.yaml`` file to help you launch chains as well as a ΛCDM proposal matrix in the ``cobaya/`` folder. This template shows how to combine 18 likelihoods (13 T&E and 5 lensing) with cobaya to forecasts cosmological parameter constraints from Ext-10k.

===================

.. |NSF| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/NSF.jpg
   :alt: NSF
   :height: 150px

.. |USAP| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/USAP.jpg
   :alt: USAP
   :height: 150px

.. |DOE| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/DOE.jpg
   :alt: DOE
   :height: 150px

.. |KICP| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/KICP.png
   :alt: KICP
   :height: 150px

.. |ERC| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/ERC.jpg
   :alt: ERC
   :height: 150px

.. |neucosmos| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/neucosmos_logo.png
   :alt: NEUCosmoS
   :height: 125px

.. |sorbonne| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/sorbonne_logo.jpeg
   :alt: Sorbonne
   :height: 100px

.. |IAP| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/IAP_logo.png
   :alt: IAP
   :height: 100px

.. |cnrs| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/cnrs_logo.jpeg
   :alt: CNRS
   :height: 150px

.. |argonne| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/argonne.jpg
   :alt: Argonne
   :height: 100px

.. |fermilab| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/fermilab.jpg
   :alt: Fermilab
   :height: 80px

.. |case_western| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/case_western.jpg
   :alt: Case Western
   :height: 100px

.. |mcgill| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/mcgill.jpg
   :alt: McGill
   :height: 100px

.. |melb| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/melb.jpg
   :alt: Melbourne
   :height: 100px

.. |michigan| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/michigan.jpg
   :alt: Michigan
   :height: 100px

.. |SLAC| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/SLAC.jpg
   :alt: SLAC
   :height: 80px

.. |stanford| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/stanford.jpg
   :alt: Stanford
   :height: 125px

.. |berkeley| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/berkeley.jpg
   :alt: Berkeley
   :height: 80px

.. |davis| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/davis.jpg
   :alt: Davis
   :height: 100px

.. |chicago| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/chicago.jpg
   :alt: Chicago
   :height: 100px

.. |boulder| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/boulder.jpg
   :alt: Boulder
   :height: 100px

.. |uoi| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/uoi.jpg
   :alt: University of Illinois
   :height: 100px

.. |caps| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/caps.png
   :alt: CAPS
   :height: 100px

.. |harvard| image:: https://github.com/SouthPoleTelescope/spt_candl_data/raw/main/logos/sponsors_institutions/harvard.jpg
   :alt: Harvard
   :height: 100px

|NSF| |USAP| |DOE| |ERC| |cnrs|

|IAP| |neucosmos| |sorbonne|

|chicago| |davis| |mcgill|

|berkeley| |stanford| |SLAC|

|fermilab| |argonne|

|melb| |michigan| |case_western| 

|uoi| |caps|

|boulder| |harvard|
