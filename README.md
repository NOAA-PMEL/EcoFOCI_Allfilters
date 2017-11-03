# EcoFOCI_AllFilters

*** Reproduction of EPIC allfilts

`
 Running Version 1.15 10/07/05 ...

 ****************************************************
 *                A L L F I L T S                   *
 *                                                  *
 * Applies digital filter and decimates time series *
 * NOTE: The input time increment (DT) must be a    *
 * multiple of 60 minutes for filter 9 or 10.       *
 *                                                  *
 * AVAILABLE FILTERS                                *
 *                                                  *
 *  1 Symmetric Digital Filter(User enters weights) *
 *  2 Ideal Filter (cosine taper between 2 freqs)   *
 *  3 Godin filter (input DT must be <= 60min)      *
 *  4 Running Gaussian filter                       *
 *  5 Bartlett (triangular) filter                  *
 *  6 Hanning full cosine filter, -pi to pi         *
 *  7 Parzen half cosine filter, -pi/2 to pi/2      *
 *  8 Hamming Band-pass filter                      *
 *  9 2.86-hr lowpass Lanczos cosine-squared filter *
 * 10 35-hr   lowpass Lanczos cosine-squared filter *
 `

 file or pointer file 

 output summary file


 ###
 should automatically decimate if option 0 is chosen with user entered dt

 use flags instead of menu

 time series filters (monthly, daily, annual)


Read data into xarray (netcdf)

either as epic compatible time or as cf compatible time (flag)
 filters available:

 - time filters 
 	* these are xarray / pandas wrappers

 - lanzcos 35hr lowpass filter


################

Legal Disclaimer

This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration (NOAA), or the United States Department of Commerce (DOC). All NOAA GitHub project code is provided on an 'as is' basis and the user assumes responsibility for its use. Any claims against the DOC or DOC bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation, or favoring by the DOC. The DOC seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by the DOC or the United States Government.
