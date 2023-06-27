import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read and convert to datetime the generation files
df_P_100 = pd.read_csv("P_100.csv")
df_P_150 = pd.read_csv("P_150.csv")
df_P_PV = pd.read_csv("P_PV.csv")

df_P_100['time'] = pd.to_datetime(df_P_100['time'], utc=True)
df_P_150['time'] = pd.to_datetime(df_P_150['time'], utc=True)
df_P_PV['time'] = pd.to_datetime(df_P_PV['time'], utc=True)

def out_year_timeseries_100(sel_year, locations):
    # Filter the column 'time' inside df_P_100_year for the chosen year
    df_P_100_year = df_P_100[df_P_100['time'].dt.year == sel_year]
    
    # Create a dictionary to store the time series data for each location
    time_series = pd.DataFrame()
    
    # Get the time series data for each location
    for location in locations:
        time_series[location] = df_P_100_year[location]
    
    return time_series

sel_year = 2012
locs_w = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.1', 'LOC_5.1','LOC_6', 'LOC_7', 'LOC_8.1','LOC_9', 'LOC_10']
locs_s = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.2', 'LOC_5.2','LOC_6', 'LOC_7', 'LOC_8.2','LOC_9', 'LOC_10']
time_series_data_100 = out_year_timeseries_100(sel_year, locs_w)

loc_data_series_100 = pd.DataFrame()
for location, series in time_series_data_100.items():
    loc_data_series_100[location] = series

df_P_100_year = df_P_100[df_P_100['time'].dt.year == sel_year]
cap_inst= 50
P_100_1_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_1': loc_data_series_100['LOC_1'][24:-24]* cap_inst})
P_100_2_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_2': loc_data_series_100['LOC_2'][24:-24]* cap_inst})
P_100_3_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_3': loc_data_series_100['LOC_3'][24:-24]* cap_inst})
P_100_4_1_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_4_1': loc_data_series_100['LOC_4.1'][24:-24]* cap_inst})
P_100_5_1_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_5_1': loc_data_series_100['LOC_5.1'][24:-24]* cap_inst})
P_100_6_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_6': loc_data_series_100['LOC_6'][24:-24]* cap_inst})
P_100_7_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_7': loc_data_series_100['LOC_7'][24:-24]* cap_inst})
P_100_8_1_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_8_1': loc_data_series_100['LOC_8.1'][24:-24]* cap_inst})
P_100_9_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_9': loc_data_series_100['LOC_9'][24:-24]* cap_inst})
P_100_10_data = pd.DataFrame({'time': df_P_100_year['time'][24:-24], 'LOC_10': loc_data_series_100['LOC_10'][24:-24]* cap_inst})

def out_year_timeseries_150(sel_year, locations):
    # Filter the column 'time' inside df_P_150_year for the chosen year
    df_P_150_year = df_P_150[df_P_150['time'].dt.year == sel_year]
    
    # Create a dictionary to store the time series data for each location
    time_series = pd.DataFrame()
    
    # Get the time series data for each location
    for location in locations:
        time_series[location] = df_P_150_year[location]
    
    return time_series

# sel_year = 2012
locs_w = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.1', 'LOC_5.1', 'LOC_6', 'LOC_7', 'LOC_8.1', 'LOC_9', 'LOC_10']
locs_s = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.2', 'LOC_5.2', 'LOC_6', 'LOC_7', 'LOC_8.2', 'LOC_9', 'LOC_10']
time_series_data_150 = out_year_timeseries_150(sel_year, locs_w)

loc_data_series_150 = pd.DataFrame()
for location, series in time_series_data_150.items():
    loc_data_series_150[location] = series
    
df_P_150_year = df_P_150[df_P_150['time'].dt.year == sel_year]
P_150_1_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_1': loc_data_series_150['LOC_1'][24:-24]* cap_inst})
P_150_2_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_2': loc_data_series_150['LOC_2'][24:-24]* cap_inst})
P_150_3_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_3': loc_data_series_150['LOC_3'][24:-24]* cap_inst})
P_150_4_1_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_4_1': loc_data_series_150['LOC_4.1'][24:-24]* cap_inst})
P_150_5_1_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_5_1': loc_data_series_150['LOC_5.1'][24:-24]* cap_inst})
P_150_6_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_6': loc_data_series_150['LOC_6'][24:-24]* cap_inst})
P_150_7_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_7': loc_data_series_150['LOC_7'][24:-24]* cap_inst})
P_150_8_1_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_8_1': loc_data_series_150['LOC_8.1'][24:-24]* cap_inst})
P_150_9_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_9': loc_data_series_150['LOC_9'][24:-24]* cap_inst})
P_150_10_data = pd.DataFrame({'time': df_P_150_year['time'][24:-24], 'LOC_10': loc_data_series_150['LOC_10'][24:-24]* cap_inst})

def out_year_timeseries_PV(sel_year, locations):
    # Filter the column 'time' inside df_P_PV for the chosen year
    df_P_PV_year = df_P_PV[df_P_PV['time'].dt.year == sel_year]
    
    # Create a dictionary to store the time series data for each location
    time_series = pd.DataFrame()
    
    # Get the time series data for each location
    for location in locations:
        time_series[location] = df_P_PV_year[location]
    
    return time_series

# sel_year = 2012
locs_w = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.1', 'LOC_5.1', 'LOC_6', 'LOC_7', 'LOC_8.1', 'LOC_9', 'LOC_10']
locs_s = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.2', 'LOC_5.2', 'LOC_6', 'LOC_7', 'LOC_8.2', 'LOC_9', 'LOC_10']
time_series_data_PV = out_year_timeseries_PV(sel_year, locs_s)

loc_data_series_PV = pd.DataFrame()
for location, series in time_series_data_PV.items():
    loc_data_series_PV[location] = series
    
df_P_PV_year = df_P_PV[df_P_PV['time'].dt.year == sel_year]
P_PV_1_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_1': loc_data_series_PV['LOC_1'][24:-24]* cap_inst})
P_PV_2_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_2': loc_data_series_PV['LOC_2'][24:-24]* cap_inst})
P_PV_3_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_3': loc_data_series_PV['LOC_3'][24:-24]* cap_inst})
P_PV_4_2_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_4_2': loc_data_series_PV['LOC_4.2'][24:-24]* cap_inst})
P_PV_5_2_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_5_2': loc_data_series_PV['LOC_5.2'][24:-24]* cap_inst})
P_PV_6_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_6': loc_data_series_PV['LOC_6'][24:-24]* cap_inst})
P_PV_7_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_7': loc_data_series_PV['LOC_7'][24:-24]* cap_inst})
P_PV_8_2_data = pd.DataFrame({'time': df_P_PV_year['time'][24:-24], 'LOC_8_2': loc_data_series_PV['LOC_8.2'][24:-24]* cap_inst})

# Capacity Factors
#  by definition: The ratio of the electrical energy produced by a generating unit for the period of time considered to the electrical energy that could have been produced at continuous full power operation during the same period.
# CF P_100
# CF_100_1_data = (P_100_1_data.sum() / (cap_inst * 8736)) * 100
# CF_100_1 = f'{CF_100_1_data.item():.2f}%'
locs_w = ['LOC_1', 'LOC_2', 'LOC_3', 'LOC_4.1', 'LOC_5.1', 'LOC_6', 'LOC_7', 'LOC_8.1', 'LOC_9', 'LOC_10']
CF_100 = {}
CF_150 = {}
for loc in locs_w:
    P_100data = df_P_100_year[loc][24:-24]*cap_inst
    # CF_100data = (P_100data.sum() / (cap_inst * 8736))
    CF_100data = (P_100data.sum() / (cap_inst * 8736))
    CF100 = f'{CF_100data.item() * 100:.2f}%'
    CF_100[loc] = CF100
    P_150data = df_P_150_year[loc][24:-24]*cap_inst
    CF_150data = (P_150data.sum() / (cap_inst * 8736))
    CF150 = f'{CF_150data.item() * 100:.2f}%'
    CF_150[loc] = CF150

CF_PV = {}
for loc in locs_s:
    P_s_data = df_P_PV_year[loc][24:-24]*cap_inst
    CF_PVdata = (P_s_data.sum() / (cap_inst * 8736))
    CFPV = f'{CF_PVdata.item()*100:.2f}%'
    CF_PV[loc] = CFPV
    
print(CF_PV)