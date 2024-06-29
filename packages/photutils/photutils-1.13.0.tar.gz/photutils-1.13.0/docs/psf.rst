.. _psf-photometry:

PSF Photometry (`photutils.psf`)
================================

The `photutils.psf` subpackage contains tools for model-fitting
photometry, often called "PSF photometry".

.. _psf-terminology:


Terminology
-----------
Different astronomy subfields use the terms "PSF", "PRF", or related
terms somewhat differently, especially when colloquial usage is taken
into account. This package aims to be at the very least internally
consistent, following the definitions described here.

We take the Point Spread Function (PSF), or instrumental Point
Spread Function (iPSF) to be the infinite-resolution and
infinite-signal-to-noise flux distribution from a point source on
the detector, after passing through optics, dust, atmosphere, etc.
By contrast, the function describing the responsivity variations
across individual *pixels* is the Pixel Response Function (sometimes
called "PRF", but that acronym is not used here for reasons that will
soon be apparent). The convolution of the PSF and pixel response
function, when discretized onto the detector (i.e., a rectilinear
CCD grid), is the effective PSF (ePSF) or Point Response Function
(PRF) (this latter terminology is the definition used by `Spitzer
<https://irsa.ipac.caltech.edu/data/SPITZER/docs/dataanalysistools/tools
/mopex/mopexusersguide/89/>`_). In many cases the PSF/ePSF/PRF
distinction is unimportant, and the ePSF/PRF are simply called
the "PSF", but the distinction can be critical when dealing
carefully with undersampled data or detectors with significant
intra-pixel sensitivity variations. For a more detailed
description of this formalism, see `Anderson & King 2000
<https://ui.adsabs.harvard.edu/abs/2000PASP..112.1360A/abstract>`_.

All this said, in colloquial usage "PSF photometry" sometimes refers
to the more general task of model-fitting photometry (with the effects
of the PSF either implicitly or explicitly included in the models),
regardless of exactly what kind of model is actually being fit. For
brevity (e.g., ``photutils.psf``), we use "PSF photometry" in this way,
as a shorthand for the general approach.


PSF Photometry
--------------

Photutils provides a modular set of tools to perform PSF photometry
for different science cases. The tools are implemented as classes that
perform various subtasks of PSF photometry. High-level classes are also
provided to connect these pieces together.

The two main PSF-photometry classes are `~photutils.psf.PSFPhotometry`
and `~photutils.psf.IterativePSFPhotometry`.
`~photutils.psf.PSFPhotometry` provides the framework for a flexible PSF
photometry workflow that can find sources in an image, optionally group
overlapping sources, fit the PSF model to the sources, and subtract the
fit PSF models from the image. `~photutils.psf.IterativePSFPhotometry`
is an iterative version of `~photutils.psf.PSFPhotometry` where
after the fit sources are subtracted, the process repeats until no
additional sources are detected or a maximum number of iterations has
been reached. When used with the `~photutils.detection.DAOStarFinder`,
`~photutils.psf.IterativePSFPhotometry` is essentially an implementation
of the DAOPHOT algorithm described by Stetson in his `seminal paper
<https://ui.adsabs.harvard.edu/abs/1987PASP...99..191S/abstract>`_ for
crowded-field stellar photometry.

The star-finding step is controlled by the ``finder``
keyword, where one inputs a callable function or class
instance. Typically, this would be one of the star-detection
classes implemented in the `photutils.detection`
subpackage, e.g., `~photutils.detection.DAOStarFinder`,
`~photutils.detection.IRAFStarFinder`, or
`~photutils.detection.StarFinder`.

After finding sources, one can optionally apply a clustering algorithm
to group overlapping sources using the ``grouper`` keyword. Usually,
groups are formed by a distance criterion, which is the case of the
grouping algorithm proposed by Stetson. Stars that grouped are fit
simultaneously. The reason behind the construction of groups and not
fitting all stars simultaneously is illustrated as follows: imagine
that one would like to fit 300 stars and the model for each star has
three parameters to be fitted. If one constructs a single model to fit
the 300 stars simultaneously, then the optimization algorithm will
have to search for the solution in a 900-dimensional space, which
is computationally expensive and error-prone. Having smaller groups
of stars effectively reduces the dimension of the parameter space,
which facilitates the optimization process. For more details see
:ref:`psf-grouping`.

The local background around each source can optionally be subtracted
using the ``localbkg_estimator`` keyword. This keyword accepts a
`~photutils.background.LocalBackground` instance that estimates the
local statistics in a circular annulus aperture centered on each source.
The size of the annulus and the statistic function can be configured in
`~photutils.background.LocalBackground`.

The next step is to fit the sources and/or groups. This
task is performed using an astropy fitter, for example
`~astropy.modeling.fitting.LevMarLSQFitter`, input via the ``fitter``
keyword. The shape of the region to be fitted can be configured using
the ``fit_shape`` parameter. In general, ``fit_shape`` should be set
to a small size (e.g., (5, 5)) that covers the central star region
with the highest flux signal-to-noise. The initial positions are
derived from the ``finder`` algorithm. The initial flux values for the
fit are derived from measuring the flux in a circular aperture with
radius ``aperture_radius``. The initial positions and fluxes can be
alternatively input in a table via the ``init_params`` keyword when
calling the class.

After sources are fitted, a model image of the fit
sources or a residual image can be generated using the
:meth:`~photutils.psf.PSFPhotometry.make_model_image` and
:meth:`~photutils.psf.PSFPhotometry.make_residual_image` methods,
respectively.

For `~photutils.psf.IterativePSFPhotometry`, the above steps can be
repeated until no additional sources are detected (or until a maximum
number of iterations).

The `~photutils.psf.PSFPhotometry` and
`~photutils.psf.IterativePSFPhotometry` classes provide the structure
in which the PSF-fitting steps described above are performed, but
all the stages can be turned on or off or replaced with different
implementations as the user desires. This makes the tools very flexible.
One can also bypass several of the steps by directly inputting to
``init_params`` an astropy table containing the initial parameters for
the source centers, fluxes, group identifiers, and local backgrounds.
This is also useful if one is interested in fitting only one or a few
sources in an image.

Example Usage
-------------

Let's start with a simple example using simulated stars whose PSF is
assumed to be Gaussian. We'll create a synthetic image using tools
provided by the :ref:`photutils.datasets <datasets>` module:

.. doctest-requires:: scipy

    >>> import numpy as np
    >>> from photutils.datasets import make_noise_image
    >>> from photutils.psf import IntegratedGaussianPRF, make_psf_model_image
    >>> psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    >>> psf_shape = (9, 9)
    >>> n_sources = 10
    >>> shape = (101, 101)
    >>> data, true_params = make_psf_model_image(shape, psf_model, n_sources,
    ...                                          model_shape=psf_shape,
    ...                                          flux=(500, 700),
    ...                                          min_separation=10, seed=0)
    >>> noise = make_noise_image(data.shape, mean=0, stddev=1, seed=0)
    >>> data += noise
    >>> error = np.abs(noise)

Let's plot the image:

.. plot::

    import matplotlib.pyplot as plt
    from photutils.datasets import make_noise_image
    from photutils.psf import IntegratedGaussianPRF, make_psf_model_image

    psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    psf_shape = (9, 9)
    n_sources = 10
    shape = (101, 101)
    data, true_params = make_psf_model_image(shape, psf_model, n_sources,
                                             model_shape=psf_shape,
                                             flux=(500, 700),
                                             min_separation=10, seed=0)
    noise = make_noise_image(data.shape, mean=0, stddev=1, seed=0)
    data += noise
    plt.imshow(data, origin='lower')
    plt.title('Simulated Data')
    plt.colorbar()


Fitting multiple stars
^^^^^^^^^^^^^^^^^^^^^^

Now let's use `~photutils.psf.PSFPhotometry` to perform PSF photometry
on the stars in this image. Note that the input image must be
background-subtracted prior to using the photometry classes. See
:ref:`background` for tools to subtract a global background from an
image. This is not needed for our synthetic image because it does not
include background.

We'll use the `~photutils.detection.DAOStarFinder` class for
source detection. We'll estimate the initial fluxes of each
source using a circular aperture with a radius 4 pixels. The
central 5x5 pixel region of each star will be fit using an
`~photutils.psf.IntegratedGaussianPRF` PSF model. First, let's create an
instance of the `~photutils.psf.PSFPhotometry` class:

.. doctest-requires:: scipy

    >>> from photutils.detection import DAOStarFinder
    >>> from photutils.psf import PSFPhotometry
    >>> psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    >>> fit_shape = (5, 5)
    >>> finder = DAOStarFinder(6.0, 2.0)
    >>> psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
    ...                         aperture_radius=4)

To perform the PSF fitting, we then call the class instance
on the data array, and optionally an error and mask array. A
`~astropy.nddata.NDData` object holding the data, error, and mask arrays
can also be input into the ``data`` parameter. Note that all non-finite
(e.g., NaN or inf) data values are automatically masked. Here we input
the data and error arrays:

.. doctest-requires:: scipy

    >>> phot = psfphot(data, error=error)

A table of initial PSF model parameter values can also be input when
calling the class instance. An example of that is shown later.

Equivalently, one can input an `~astropy.nddata.NDData` object with any
uncertainty object that can be converted to standard-deviation errors:

.. doctest-skip::

    >>> from astropy.nddata import NDData, StdDevUncertainty
    >>> uncertainty = StdDevUncertainty(error)
    >>> nddata = NDData(data, uncertainty=uncertainty)
    >>> phot2 = psfphot(nddata)

The result is an astropy `~astropy.table.Table` with columns for the
source and group identification numbers, the x, y, and flux initial,
fit, and error values, local background, number of unmasked pixels
fit, the group size, quality-of-fit metrics, and flags. See the
`~photutils.psf.PSFPhotometry` documentation for descriptions of the
output columns.

The full table cannot be shown here as it has many columns, but let's
print the source ID along with the fit x, y, and flux values:

.. doctest-requires:: scipy

    >>> phot['x_fit'].info.format = '.4f'  # optional format
    >>> phot['y_fit'].info.format = '.4f'
    >>> phot['flux_fit'].info.format = '.4f'
    >>> print(phot[('id', 'x_fit', 'y_fit', 'flux_fit')])  # doctest: +FLOAT_CMP
     id  x_fit   y_fit  flux_fit
    --- ------- ------- --------
      1 54.5658  7.7644 514.0129
      2 29.0865 25.6111 536.5818
      3 79.6281 28.7487 618.7551
      4 63.2340 48.6408 563.3426
      5 88.8848 54.1202 619.8874
      6 79.8763 61.1380 648.1679
      7 90.9606 72.0861 601.8609
      8  7.8038 78.5734 635.6392
      9  5.5350 89.8870 539.6850
     10 71.8414 90.5842 692.3331

Let's create the residual image:

.. doctest-requires:: scipy

    >>> resid = psfphot.make_residual_image(data, (9, 9))

and plot it:

.. plot::

    import matplotlib.pyplot as plt
    import numpy as np
    from astropy.visualization import simple_norm
    from photutils.datasets import make_noise_image
    from photutils.detection import DAOStarFinder
    from photutils.psf import (IntegratedGaussianPRF, PSFPhotometry,
                               make_psf_model_image)

    psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    psf_shape = (9, 9)
    n_sources = 10
    shape = (101, 101)

    data, true_params = make_psf_model_image(shape, psf_model, n_sources,
                                             model_shape=psf_shape,
                                             flux=(500, 700),
                                             min_separation=10, seed=0)
    noise = make_noise_image(data.shape, mean=0, stddev=1, seed=0)
    data += noise
    error = np.abs(noise)

    psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    fit_shape = (5, 5)
    finder = DAOStarFinder(6.0, 2.0)
    psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
                            aperture_radius=4)
    phot = psfphot(data, error=error)

    resid = psfphot.make_residual_image(data, (9, 9))

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    norm = simple_norm(data, 'sqrt', percent=99)
    ax[0].imshow(data, origin='lower', norm=norm)
    ax[1].imshow(data - resid, origin='lower', norm=norm)
    im = ax[2].imshow(resid, origin='lower')
    ax[0].set_title('Data')
    ax[1].set_title('Model')
    ax[2].set_title('Residual Image')
    plt.tight_layout()

The residual image looks like noise, indicating good fits to the
sources.

Further details about the PSF fitting can be obtained from attributes on
the `~photutils.psf.PSFPhotometry` instance. For example, the results
from the ``finder`` instance called during PSF fitting can be accessed
using the ``finder_results`` attribute (the ``finder`` returns an
astropy table):

.. doctest-requires:: scipy

    >>> psfphot.finder_results['xcentroid'].info.format = '.4f'  # optional format
    >>> psfphot.finder_results['ycentroid'].info.format = '.4f'  # optional format
    >>> psfphot.finder_results['sharpness'].info.format = '.4f'  # optional format
    >>> psfphot.finder_results['peak'].info.format = '.4f'
    >>> psfphot.finder_results['flux'].info.format = '.4f'
    >>> psfphot.finder_results['mag'].info.format = '.4f'
    >>> print(psfphot.finder_results)  # doctest: +FLOAT_CMP
     id xcentroid ycentroid sharpness ... sky   peak   flux    mag
    --- --------- --------- --------- ... --- ------- ------ -------
      1   54.5301    7.7460    0.6002 ... 0.0 53.4082 6.9430 -2.1039
      2   29.0927   25.5994    0.5950 ... 0.0 56.9892 7.5179 -2.1902
      3   79.6186   28.7516    0.5953 ... 0.0 65.4845 8.5872 -2.3346
      4   63.2485   48.6135    0.5797 ... 0.0 58.1835 7.6933 -2.2153
      5   88.8820   54.1311    0.5943 ... 0.0 68.9214 9.3947 -2.4322
      6   79.8728   61.1207    0.6212 ... 0.0 73.8172 9.7648 -2.4742
      7   90.9621   72.0803    0.6163 ... 0.0 68.1552 9.1005 -2.3977
      8    7.7962   78.5467    0.5975 ... 0.0 65.9807 8.4028 -2.3111
      9    5.5854   89.8663    0.5737 ... 0.0 54.1899 7.0039 -2.1134
     10   71.8303   90.5626    0.6034 ... 0.0 73.3127 9.5152 -2.4460

The ``fit_results`` attribute contains a dictionary with detailed
information returned from the ``fitter`` for each source:

.. doctest-requires:: scipy

    >>> psfphot.fit_results.keys()
    dict_keys(['fit_infos', 'fit_error_indices'])

The ``fit_error_indices`` key contains the indices of sources for which
the fit reported warnings or errors.

As an example, let's print the covariance matrix of the fit parameters
for the first source (note that not all astropy fitters will return a
covariance matrix):

.. doctest-skip::

    >>> psfphot.fit_results['fit_infos'][0]['param_cov']  # doctest: +FLOAT_CMP
    array([[ 7.27034774e-01,  8.86845334e-04,  3.98593038e-03],
           [ 8.86845334e-04,  2.92871525e-06, -6.36805464e-07],
           [ 3.98593038e-03, -6.36805464e-07,  4.29520185e-05]])


Fitting a single source
^^^^^^^^^^^^^^^^^^^^^^^

In some cases, one may want to fit only a single source (or few sources)
in an image. We can do that by defining a table of the sources that
we want to fit. For this example, let's fit the single star at ``(x,
y) = (42, 36)``. We first define a table with this position and then
pass that table into the ``init_params`` keyword when calling the PSF
photometry class on the data:

.. doctest-requires:: scipy

    >>> from astropy.table import QTable
    >>> init_params = QTable()
    >>> init_params['x'] = [63]
    >>> init_params['y'] = [49]
    >>> phot = psfphot(data, error=error, init_params=init_params)

The PSF photometry class allows for flexible input column names
using a heuristic to identify the x, y, and flux columns. See
`~photutils.psf.PSFPhotometry` for more details.

The output table contains only the fit results for the input source:

.. doctest-requires:: scipy

    >>> phot['x_fit'].info.format = '.4f'  # optional format
    >>> phot['y_fit'].info.format = '.4f'
    >>> phot['flux_fit'].info.format = '.4f'
    >>> print(phot[('id', 'x_fit', 'y_fit', 'flux_fit')])  # doctest: +FLOAT_CMP
     id  x_fit   y_fit  flux_fit
    --- ------- ------- --------
      1 63.2340 48.6408 563.3426

Finally, let's show the residual image. The red circular aperture shows
the location of the star that was fit and subtracted.

.. plot::

    import matplotlib.pyplot as plt
    import numpy as np
    from astropy.table import QTable
    from astropy.visualization import simple_norm
    from photutils.aperture import CircularAperture
    from photutils.datasets import make_noise_image
    from photutils.detection import DAOStarFinder
    from photutils.psf import (IntegratedGaussianPRF, PSFPhotometry,
                               make_psf_model_image)

    psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    psf_shape = (9, 9)
    n_sources = 10
    shape = (101, 101)

    data, true_params = make_psf_model_image(shape, psf_model, n_sources,
                                             model_shape=psf_shape,
                                             flux=(500, 700),
                                             min_separation=10, seed=0)
    noise = make_noise_image(data.shape, mean=0, stddev=1, seed=0)
    data += noise
    error = np.abs(noise)

    psf_model = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    fit_shape = (5, 5)
    finder = DAOStarFinder(6.0, 2.0)
    psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
                            aperture_radius=4)

    init_params = QTable()
    init_params['x'] = [63]
    init_params['y'] = [49]
    phot = psfphot(data, error=error, init_params=init_params)

    resid = psfphot.make_residual_image(data, (9, 9))
    aper = CircularAperture(zip(phot['x_fit'], phot['y_fit']), r=4)

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    norm = simple_norm(data, 'sqrt', percent=99)
    ax[0].imshow(data, origin='lower', norm=norm)
    ax[1].imshow(data - resid, origin='lower', norm=norm)
    im = ax[2].imshow(resid, origin='lower')
    ax[0].set_title('Data')
    aper.plot(ax=ax[0], color='red')
    ax[1].set_title('Model')
    aper.plot(ax=ax[1], color='red')
    ax[2].set_title('Residual Image')
    aper.plot(ax=ax[2], color='red')
    plt.tight_layout()


Forced Photometry
^^^^^^^^^^^^^^^^^

In general, the three parameters fit for each source are the x and
y positions and the flux. However, the astropy modeling and fitting
framework allows any of these parameters to be fixed during the fitting.

Let's say you want to fix the (x, y) position for each source. You can
do that by setting the ``fixed`` attribute on the model parameters:

.. doctest-requires:: scipy

    >>> psf_model2 = IntegratedGaussianPRF(flux=1, sigma=2.7 / 2.35)
    >>> psf_model2.x_0.fixed = True
    >>> psf_model2.y_0.fixed = True
    >>> psf_model2.fixed
    {'flux': False, 'x_0': True, 'y_0': True, 'sigma': True}

Now when the model is fit, the flux will be varied but, the (x, y)
position will be fixed at its initial position for every source. Let's
just fit a single source (defined in ``init_params``):

.. doctest-requires:: scipy

    >>> psfphot = PSFPhotometry(psf_model2, fit_shape, finder=finder,
    ...                         aperture_radius=4)
    >>> phot = psfphot(data, error=error, init_params=init_params)

The output table shows that the (x, y) position was unchanged, with the
fit values being identical to the initial values. However, the flux was
fit:

.. doctest-requires:: scipy

    >>> phot['flux_init'].info.format = '.4f'  # optional format
    >>> phot['flux_fit'].info.format = '.4f'
    >>> print(phot[('id', 'x_init', 'y_init', 'flux_init', 'x_fit',
    ...             'y_fit', 'flux_fit')])  # doctest: +FLOAT_CMP
     id x_init y_init flux_init x_fit y_fit flux_fit
    --- ------ ------ --------- ----- ----- --------
      1     63     49  556.4444  63.0  49.0 500.4789


Source Grouping
^^^^^^^^^^^^^^^

Source grouping is an optional feature. To turn it on, create a
`~photutils.psf.SourceGrouper` instance and input it via the ``grouper``
keyword. Here we'll group stars that are within 20 pixels of each
other:

.. doctest-requires:: scipy, sklearn

    >>> from photutils.psf import SourceGrouper
    >>> grouper = SourceGrouper(min_separation=20)
    >>> psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
    ...                         grouper=grouper, aperture_radius=4)
    >>> phot = psfphot(data, error=error)

The ``group_id`` column shows that six groups were identified (each with
two stars). The stars in each group were simultaneously fit.

.. doctest-requires:: scipy, sklearn

    >>> print(phot[('id', 'group_id', 'group_size')])
     id group_id group_size
    --- -------- ----------
      1        1          1
      2        2          1
      3        3          1
      4        4          1
      5        5          3
      6        5          3
      7        5          3
      8        6          2
      9        6          2
     10        7          1

Care should be taken in defining the star groups. As noted above,
simultaneously fitting very large star groups is computationally
expensive and error-prone. A warning will be raised if the number of
sources in a group exceeds 25.


Local Background Subtraction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To subtract a local background from each source, define a
`~photutils.background.LocalBackground` instance and input it via
the ``localbkg_estimator`` keyword. Here we'll use an annulus with
an inner and outer radius of 5 and 10 pixels, respectively, with the
`~photutils.background.MMMBackground` statistic (with its default sigma
clipping):

.. doctest-requires:: scipy, sklearn

    >>> from photutils.background import LocalBackground, MMMBackground
    >>> bkgstat = MMMBackground()
    >>> localbkg_estimator = LocalBackground(5, 10, bkgstat)
    >>> finder = DAOStarFinder(10.0, 2.0)
    >>> psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
    ...                         grouper=grouper, aperture_radius=4,
    ...                         localbkg_estimator=localbkg_estimator)
    >>> phot = psfphot(data, error=error)

The local background values are output in the table:

.. doctest-requires:: scipy, sklearn

    >>> phot['local_bkg'].info.format = '.4f'  # optional format
    >>> print(phot[('id', 'local_bkg')])  # doctest: +FLOAT_CMP
     id local_bkg
    --- ---------
      1   -0.0840
      2    0.1784
      3    0.2593
      4   -0.0574
      5    0.2934
      6   -0.0826
      7   -0.1130
      8   -0.2138
      9    0.0089
     10    0.3926

The local background values can also be input directly using the
``init_params`` keyword.


Iterative PSF Photometry
^^^^^^^^^^^^^^^^^^^^^^^^

Now let's use the `~photutils.psf.IterativePSFPhotometry` class to
iteratively fit the stars in the image. This class is useful for crowded
fields where faint stars are very close to bright stars. The faint stars
may not be detected until after the bright stars are subtracted.

For this simple example, let's input a table of three stars for the
first fit iteration. Subsequent iterations will use the ``finder`` to
find additional stars:

.. doctest-requires:: scipy

    >>> from photutils.background import LocalBackground, MMMBackground
    >>> from photutils.psf import IterativePSFPhotometry
    >>> fit_shape = (5, 5)
    >>> finder = DAOStarFinder(10.0, 2.0)
    >>> bkgstat = MMMBackground()
    >>> localbkg_estimator = LocalBackground(5, 10, bkgstat)
    >>> init_params = QTable()
    >>> init_params['x'] = [54, 29, 80]
    >>> init_params['y'] = [8, 26, 29]
    >>> psfphot2 = IterativePSFPhotometry(psf_model, fit_shape, finder=finder,
    ...                                   localbkg_estimator=localbkg_estimator,
    ...                                   aperture_radius=4)
    >>> phot = psfphot2(data, error=error, init_params=init_params)

The table output from `~photutils.psf.IterativePSFPhotometry` contains a
column called ``iter_detected`` that returns the fit iteration in which
the source was detected:

.. doctest-requires:: scipy

    >>> phot['x_fit'].info.format = '.4f'  # optional format
    >>> phot['y_fit'].info.format = '.4f'
    >>> phot['flux_fit'].info.format = '.4f'
    >>> print(phot[('id', 'iter_detected', 'x_fit', 'y_fit', 'flux_fit')])  # doctest: +FLOAT_CMP
     id iter_detected  x_fit   y_fit  flux_fit
    --- ------------- ------- ------- --------
      1             1 54.5665  7.7641 514.2679
      2             1 29.0883 25.6092 534.0753
      3             1 79.6273 28.7479 613.0246
      4             2 63.2340 48.6415 564.1535
      5             2 88.8857 54.1203 614.6949
      6             2 79.8765 61.1358 649.9802
      7             2 90.9631 72.0881 603.7519
      8             2  7.8202 78.5821 641.7541
      9             2  5.5350 89.8869 539.5465
     10             2 71.8485 90.5830 687.4396


References
----------

`Spitzer PSF vs. PRF
<https://irsa.ipac.caltech.edu/data/SPITZER/docs/files/spitzer/PRF_vs_PSF.pdf>`_

`The Kepler Pixel Response Function
<https://ui.adsabs.harvard.edu/abs/2010ApJ...713L..97B/abstract>`_

`Stetson (1987 PASP 99, 191)
<https://ui.adsabs.harvard.edu/abs/1987PASP...99..191S/abstract>`_

`Anderson and King (2000 PASP 112, 1360)
<https://ui.adsabs.harvard.edu/abs/2000PASP..112.1360A/abstract>`_


Reference/API
-------------

.. automodapi:: photutils.psf
    :no-heading:
