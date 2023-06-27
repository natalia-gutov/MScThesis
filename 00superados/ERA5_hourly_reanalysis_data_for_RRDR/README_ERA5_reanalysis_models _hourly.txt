1. PROJECT
------------

Title: Sub-seasonal to seasonal forecasting for energy (S2S4E)
Dates: 1st December 2017 - 30th November 2020
Funding organisation: Horizon 2020
Grant no.: 776787
This project received funding from the Horizon 2020 programme under the grant agreement number 776787.

2. DATASET
------------
Title: ERA5 derived time series of European country-aggregate electricity demand, wind power generation and solar power generation: hourly data from 1979-2019 

Publication Year: 2020
Creator(s): H.C. Bloomfield, D.J. Brayshaw, A. Charlton-Perez
Organisation(s): University of Reading, National Centre for Atmospheric Science
Source(s): This dataset was created using meteorological data from the ERA5 reanalysis available from https://cds.climate.copernicus.eu/cdsapp#!/home.
Copernicus Climate Change Service (C3S) (2017): ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate. Copernicus Climate Change Service Climate Data Store (CDS), date of access: 14-01-2019. https://cds.climate.copernicus.eu/cdsapp#!/home

3. TERMS OF USE
-----------------
Copyright 2020, University of Reading. This dataset is licensed by the rights-holder(s) under a Creative Commons Attribution 4.0 International Licence: https://creativecommons.org/licenses/by/4.0/.


4. CONTENTS
------------

The demand, wind power capacity factor and solar power capacity factor data can be found in the relevant subdirectories. The weather-dependent country-level inputs to the models are also given in each sub-directory. The contents of each folder is described below.

Model_validation_data_ERA5_hourly.xlsx provides hourly validation of the full demand model, wind power capacity factors and solar power capacity factors against data from the ENTSO-e transparency platform (data available from: https://www.entsoe.eu/data/transparency-platform/) 

demand_model_outputs

ERA5_Regression_coeffs_demand_model.csv - A list of the regression coefficients that were fitted by the multiple linear regression model for each of the 29 European Countries. WD1 = Monday WD2 = Tuesday, WK1 = Saturday. HDD = heating degree days, CDD = cooling degree days. See section 5 for more details on the model.

ERA5_full_demand_all_countries_1979_2019_hourly.csv Hourly country level electricity demand for the 29 countries modelled in this study from 01/01/1979 to 31/12/2019.

ERA5_weather_dependent_demand_all_countries_1979_2019_hourly.csv Hourly level electricity weather-dependent demand for the 29 countries modelled in this study from 01/01/1979 to 31/12/2019. See section 5 for details of the definition of weather dependent.

ERA5_T2m_all_countries_1979_2019_inclusive.csv Daily country level 2m temperatures, from the ERA5 reanalysis, for the 29 countries modelled in this study from 01/01/1979 to 31/12/2019.

ERA5_HDD_all_countries_1979_2019_inclusive_hourly.csv Daily country level, heating-degree-days (HDD) for the 29 countries modelled in this study from 01/01/1979 to 31/12/2019. 

ERA5_CDD_all_countries_1979_2019_inclusive_hourly.csv Daily country level, cooling-degree-days (CDD) for the 29 countries modelled in this study from 01/01/1979 to 31/12/2019. 


wind_power_model_outputs

Enercon_E70_2300MW_turbine.csv - Type 1 power curve used in this study.
Gamesa_G87_2000MW_turbine.csv - Type 2 power curve used in this study.
Vestas_v110_2000MW_turbine.csv - Type 3 power curve used in this study.

ERA5_whh_all_countries_1979_2019_hourly.csv - Hourly wind turbine hub-height wind speeds (100m) for the 28 countries modelled in this study from 01/01/1979 to 31/12/2019. 

ERA5_wind_power_capacity_facor_all_countries_1979_2019_hourly.csv - Hourly wind power capacity factors for the 28 countries modelled in this study from 01/01/1979 to 31/12/2019. 

solar_power_model_outputs

ERA5_T2m_all_countries_1979_2019_hourly.csv Hourly 2m temperature for the 28 countries modelled in this study from 01/01/1979 to 31/12/2019.

ERA5_SWGDN_all_countries_1979_2019_hourly.csv Hourly surface shortwave radiation for the 28 countries modelled in this study from 01/01/1979 to 31/12/2019.

ERA5_solar_power_capacity_factor_all_countries_1979_2019_hourly.csv Hourly solar power capacity factor for the 28 countries modelled in this study from 01/01/1979 to 31/12/2019.


5. METHOD and PROCESSING
--------------------------

For all three of the models described below the countries modelled are: Austria, Belgium, Bulgaria, Croatia, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom. For demand Estonia is also included. Full details of the models can be found in Bloomfield et al.,(2020). A brief description of each will now follow.

Demand model

A time series of daily mean electricity demand for 28 European countries was derived from 2m temperature (T2m) data from the ERA5 reanalysis. The model was developed on a daily resolution using a multiple-linear regression model where the possible model inputs are the day of the week, heating degree days (HDD) and cooling degree days (CDD). The model is optimised to choose the best set of parameters to minimise the Akaike information criteria. Time-series of the weather-dependent model input parameters (T2m, HDD, CDD) are available as well as the full demand model output and weather-dependent demand (i.e. the demand with the effects of the day of the week removed by setting those regression coefficients to zero). The model is trained on data from the ENTSOe transparency platform from 2016-2017.


The daily-mean demand data is downscaled to hourly resolution using a prescribed diurnal cycle (see detailed method description in Bloomfield et al., (2016). A different diurnal cycle is determined for each meteorological season based on the recorded 2016 and 2017 hourly demand data. Each daily demand value is then downscaled to hourly resolution using a linear combination of relevant diurnal curves (e.g., the daily-mean demand for 1st December is downscaled using a 50%–50% weighting of the diurnal curves derived from the Meteorological-Autumn and Meteorological-Winter hourly data). 

Wind Power model

A time series of hourly wind power capacity factor for 28 European countries was derived from 100m wind speed data from the ERA5 reanalysis. The model was developed by selecting the optimal wind turbine that would be present in each re-analysis grid box based on the climatology of the 100m wind speeds. The wind power generation in each grid box was then calculated and weighted by the location of the turbines (taken from thewindpower.net database) in order to get country-aggregate wind power capacity factor data.


Solar Power model

A time series of hourly solar power capacity factor for 28 European countries was derived from 2m temperatures and surface short wave radiation data from the ERA5 reanalysis. This is an empirical model developed from the methods used in Evans and Florschuetz 1977 and Bett and Thornton (2016).


References:

Evans, D.L. and L.W. Florschuetz (1977). Cost studies on terrestrial photovoltaic power systems with sunlight concentration. Solar Energy, 19, 255-262.

Bett, P. E., & Thornton, H. E. (2016). The climatological relationships between wind and solar energy supply in Britain. Renewable Energy, vol 87 pt 1, 96-110. DOI: 10.1016/j.renene.2015.10.006.

Bloomfield, H. C., Brayshaw, D. J., & Charlton‐Perez, A. J. (2020). Characterizing the winter meteorological drivers of the European electricity system using targeted circulation types. Meteorological Applications, 27(1). DOI:10.1002/met.1858 


Bloomfield, H. C., Brayshaw, D. J., Shaffrey, L. C., Coker, P. J., & Thornton, H. E. (2016). Quantifying the increasing sensitivity of power systems to climate variability. Environmental Research Letters, 11(12), 124025. DOI: 10.1088/1748-9326/11/12/124025


Bloomfield, H. C., Gonzalez, P.L.M., Brayshaw, D. J., & Charlton‐Perez, A. J. Sub-seasonal forecasts of demand, wind power and solar power generation (in prep.) 





