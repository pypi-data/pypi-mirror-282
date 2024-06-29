# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %% [markdown]
#
# # pPXF: Fitting both photometry and spectra
#
# ![pPXF](https://www-astro.physics.ox.ac.uk/~cappellari/software/ppxf_logo.svg)
#
# ## Description
#
# Usage example for the procedure pPXF originally described in 
# [Cappellari & Emsellem (2004)](http://adsabs.harvard.edu/abs/2004PASP..116..138C),
# substantially upgraded in 
# [Cappellari (2017)](http://adsabs.harvard.edu/abs/2017MNRAS.466..798C) 
# and with the inclusion of photometry and linear constraints in 
# [Cappellari (2023)](https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.3273C).
#
# ### MODIFICATION HISTORY
#
# * V1.0.0: Michele Cappellari, Oxford, 29 March 2022: Created
# * V1.1.0: MC, Oxford, 10 June 2022: Updated for `pPXF` 8.1 using the new `ppxf_util.synthetic_photometry`
# * V1.2.0: MC, Oxford, 7 September 2022: Updated for pPXF 8.2
# * V1.3.0: MC, Oxford, 19 November 2023: Updated for pPXF 9.0 using the new `sps_util`.
#
# ___

# %%
from pathlib import Path
from urllib import request

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

from ppxf.ppxf import ppxf
import ppxf.ppxf_util as util
import ppxf.sps_util as lib

# %% [markdown]
# ## Read the observed galaxy spectrum
#
# Read the galaxy spectrum taken from [SDSS DR8](http://www.sdss3.org/dr8/).
# The spectrum is *already* log rebinned by the SDSS DR8 pipeline and log_rebin
# should not be used in this case.

# %%
file_dir = Path(lib.__file__).parent / 'spectra' / 'NGC3073_SDSS_DR8.fits'
hdu = fits.open(file_dir)[1]
t = hdu.data
redshift = float(hdu.header["Z"]) # SDSS redshift estimate

# %% [markdown]
# Only use the wavelength range in common between galaxy and stellar library

# %%
flux = t['flux']
galaxy = flux/np.median(flux)   # Normalize spectrum to avoid numerical issues
wave = t['wavelength']

# %% [markdown]
# Restricts the fit to the region sampled by the high quality MILES spectra

# %%
w = wave < 7500
galaxy = galaxy[w]
wave = wave[w]

# %% [markdown]
# The SDSS wavelengths are in vacuum, while the MILES ones are in air. For a
# rigorous treatment, the SDSS vacuum wavelengths should be converted into air
# wavelengths and the spectra should be resampled. To avoid resampling, given
# that the wavelength dependence of the correction is very weak, I approximate
# it with a constant factor.

# %%
wave *= np.median(util.vac_to_air(wave)/wave)
rms = 0.019  # rms scatter of the spectrum residuals
goodpixels = np.arange(galaxy.size)  # fit full spectrum

# %% [markdown]
# In a real situation one does not know the galaxy spectrum outside the fitted
# range. However, in this example I pass the full galaxy spectrum to pPXF even
# tough fit only a limited range of `goodpixels``. In this way I can see
# directly how well the extrapolated best fit reproduces the true galaxy
# spectrum outside the fitted range.

# %%
noise = np.full_like(galaxy, rms)

# %% [markdown]
# Estimate the wavelength fitted range in the rest frame.
# This is used to select the gas templates falling in the fitted range

# %%
wave_good = wave[goodpixels]
lam_range_gal = np.array([np.min(wave_good), np.max(wave_good)])/(1 + redshift)

# %% [markdown]
# ## Observed galaxy photometric fluxes
#
# Mean galaxy fluxes in the photometric bands `[FUV, NUV, u, g, r, i, z, J, H, K]`.
# They are normalized like the galaxy spectrum

# %%
phot_galaxy = np.array([1.23e-16, 6.23e-17, 4.19e-17, 5.67e-17, 3.90e-17, 
                        2.93e-17, 2.30e-17, 1.30e-17, 7.83e-18, 3.49e-18])  # fluxes in erg/cm^2/s/A
phot_noise = np.full_like(phot_galaxy, np.max(phot_galaxy)*0.03)  # 1sigma uncertainties of 3%

# %% [markdown]
# ## Setup spectral templates
#
# The velocity step was already chosen by the SDSS pipeline and I convert it
# below to km/s

# %%
c = 299792.458  # speed of light in km/s
d_ln_lam = np.log(wave[-1]/wave[0])/(wave.size - 1)  # Average ln_lam step
velscale = c*d_ln_lam                   # eq. (8) of Cappellari (2017)
FWHM_gal = 2.76  # SDSS has an approximate instrumental resolution FWHM of 2.76A.

# %% [markdown]
# ## Setup stellar templates 
#
# pPXF can be used with any set of SPS population templates. However, I am
# currently providing (with permission) ready-to-use template files for four
# SPS. One can just uncomment one of the four models below. The included files
# are only a subset of the SPS that can be produced with the models, and one
# should use the relevant software/website to produce different sets of SPS
# templates if needed.
#
# 1. If you use the [fsps v3.2](https://github.com/cconroy20/fsps) SPS model
#    templates, please also cite in your paper 
#    [Conroy et al. (2009)](https://ui.adsabs.harvard.edu/abs/2009ApJ...699..486C) and
#    [Conroy et al. (2010)](https://ui.adsabs.harvard.edu/abs/2010ApJ...712..833C).
#
# 2. If you use the [GALAXEV v2020](http://www.bruzual.org/bc03/) SPS model 
#    templates, please also cite in your paper 
#    [Bruzual & Charlot (2003)](https://ui.adsabs.harvard.edu/abs/2003MNRAS.344.1000B).
#
# 3. If you use the [E-MILES](http://miles.iac.es/) SPS model templates,
#    please also cite  in your paper 
#    [Vazdekis et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.3409V).
#    <font color="red">WARNING: The E-MILES models only include SPS with age > 63 Myr and
#    are not recommended for highly star forming galaxies.</font>
#
# 4. If you use the [X-Shooter Spectral Library (XSL)](http://xsl.u-strasbg.fr/) 
#    SPS model templates, please also cite in your paper 
#    [Verro et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022A%26A...661A..50V). 
#    <font color="red">WARNING: The XSL models only include SPS with age > 50 Myr and
#    are not recommended for highly star forming galaxies.</font>

# %%
sps_name = 'fsps'
# sps_name = 'galaxev'
# sps_name = 'emiles'
# sps_name = 'xsl'

# %% [markdown]
# Read SPS models file from my GitHub if not already in the pPXF package dir. I
# am not distributing the templates with pPXF anymore. The SPS model files are
# also available [this GitHub page](https://github.com/micappe/ppxf_data).

# %%
ppxf_dir = Path(lib.__file__).parent
basename = f"spectra_{sps_name}_9.0.npz"
filename = ppxf_dir / 'sps_models' / basename
if not filename.is_file():
    url = "https://raw.githubusercontent.com/micappe/ppxf_data/main/" + basename
    request.urlretrieve(url, filename)

# %% [markdown]
# I normalize the templates to `mean=1` within the FWHM of the V-band. In this
# way the weights returned by pPXF and mean values are light-weighted
# quantities

# %%
sps = lib.sps_lib(filename, velscale, FWHM_gal, norm_range=[5070, 5950])
stars_templates, ln_lam_temp = sps.templates, sps.ln_lam_temp

# %% [markdown]
# The stellar templates are reshaped below into a 2-dim array with each
# spectrum as a column, however we save the original array dimensions, which
# are needed to specify the regularization dimensions

# %%
reg_dim = sps.templates.shape[1:]
stars_templates = sps.templates.reshape(sps.templates.shape[0], -1)

# %% [markdown]
# Construct a set of Gaussian emission line templates.
#
# The `emission_lines` function defines the most common lines, but additional
# lines can be included by editing the function in the file `ppxf_util.py`.

# %%
gas_templates, gas_names, line_wave = util.emission_lines(
    sps.ln_lam_temp, lam_range_gal, FWHM_gal)

# %% [markdown]
# Combines the stellar and gaseous templates into a single array. During the
# pPXF fit they will be assigned a different kinematic COMPONENT value

# %%
templates = np.column_stack([stars_templates, gas_templates])

# %% [markdown]
# ## Setup photometric templates

# %%
bands = ['galex1500', 'galex2500', 'SDSS/u', 'SDSS/g', 'SDSS/r', 'SDSS/i', 'SDSS/z', '2MASS/J', '2MASS/H', '2MASS/K']
phot = util.synthetic_photometry(sps.lam_temp, templates, bands, redshift=redshift, quiet=1)
phot = {"templates": phot.flux, "galaxy": phot_galaxy, "noise": phot_noise, "lam": phot.lam_eff}

# %% [markdown]
# Ideally, one would like to have photometry and spectra independently
# calibrated and measured within the same aperture. However, the relative
# calibration of photometry and spectra is never sufficiently accurate. For
# this reason, I am scaling the photometry to match the spectrum, in the
# wavelength range in common.
#
# Scale photometry to match the spectrum as in Sec.6.4 of [Cappellari
# (2023)](https://ui.adsabs.harvard.edu/abs/10.1093/mnras/stad2597)
#
# First compute synthetic photometry on SDSS galaxy spectrum, which is already
# in rest-frame

# %%
p2 = util.synthetic_photometry(wave, galaxy, bands, redshift=redshift)

# %% [markdown]
# Extract the bands that fall inside the galaxy spectrum.
# Scale photometry to match the synthetic one from the SDSS spectrum
#

# %%
d = p2.flux[p2.ok]
m = phot_galaxy[p2.ok]    # p2.ok=True if band is in galaxy wavelength range
scale = (d @ m)/(m @ m)   # eq.(34) of Cappellari (2023, MNRAS)
phot_galaxy *= scale
phot_noise *= scale

# %% [markdown]
# Compute the photometric templates in the observed bands, excluding the bands
# falling outside the range covered by the templates.

# %%
p1 = util.synthetic_photometry(sps.lam_temp, templates, bands, redshift=redshift)
phot = {"templates": p1.flux[p1.ok], "lam": p1.lam_eff[p1.ok],
        "galaxy": phot_galaxy[p1.ok], "noise": phot_noise[p1.ok]}


# %% [markdown]
# ## pPXF input parameters

# %%
c = 299792.458
vel = c*np.log(1 + redshift)   # eq.(8) of Cappellari (2017)
start = [vel, 180.]     # (km/s), starting guess for [V, sigma]

# %% [markdown]
# I fit two kinematics components, one for the stars and one for the gas.
# Assign `component=0` to the stellar templates, `component=1` to the gas.

# %%
n_stars = stars_templates.shape[1]
n_gas = len(gas_names)
component = [0]*n_stars + [1]*n_gas
gas_component = np.array(component) > 0  # gas_component=True for gas templates

# %% [markdown]
# Fit (V, sig) moments=2 for both the stars and the gas

# %%
moments = [2, 2]

# %% [markdown]
# Adopt the same starting value for both the stars and the gas components

# %%
start = [start, start]

# %% [markdown]
# ## Start pPXF fit

# %%
pp = ppxf(templates, galaxy, noise, velscale, start,
          moments=moments, degree=-1, mdegree=8, lam=wave, lam_temp=sps.lam_temp, regul=1/rms,
          reg_dim=reg_dim, component=component, gas_component=gas_component, reddening=0, 
          gas_names=gas_names, goodpixels=goodpixels, phot=phot)

# %% [markdown]
# ## Plot fit results for stars, gas and stellar population

# %%
light_weights = pp.weights[~gas_component]      # Exclude weights of the gas templates
light_weights = light_weights.reshape(reg_dim)  # Reshape to (n_ages, n_metal)
light_weights /= light_weights.sum()            # Normalize to light fractions

# %% [markdown]
# Given that the templates are normalized to the V-band, the `pPXF` weights
# represent V-band light fractions and the computed ages and metallicities
# below are also light weighted in the V-band.

# %%
sps.mean_age_metal(light_weights);
sps.mass_to_light(light_weights, band='SDSS/r', redshift=redshift);

# %%
plt.figure(figsize=(10,5))
plt.subplot(211)
pp.plot(phot=False, gas_clip=True)
plt.title(f"pPXF fit with {sps_name} SPS templates")
plt.subplot(212)
pp.plot(spec=False, gas_clip=True)
plt.tight_layout()

plt.figure(figsize=(10,3))
sps.plot(light_weights)
plt.title("Light Fraction")
plt.tight_layout()
plt.pause(5);
