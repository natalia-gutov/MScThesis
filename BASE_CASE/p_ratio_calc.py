import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os

# List of countries and years
countries = ["Germany", "France", "Belgium", "Poland", "Finland", "Netherlands", "Denmark"]
years = range(2015, 2023)
folder_path = "historical_data"

# Create a dictionary to store the data frames
data_frames = {}

# Read CSV files
for country in countries:
    country_data_frames = []
    
    for year in years:
        file_name = f"energy-charts_Public_net_electricity_generation_in_{country}_in_{year}.csv"
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            df = df.dropna(subset=["Date (UTC)"])
            # hourly frequency
            df["Date (UTC)"] = pd.to_datetime(df["Date (UTC)"])
            # df = df[df["Date (UTC)"].dt.strftime("%Y-%m-%dT%H:%M:%S%z").str.endswith("00:00")]
            # df = df[df["Date (UTC)"].dt.strftime("%Y-%m-%dT%H:00+00:00")]
            country_data_frames.append(df)
            # print(f"File: {file_path}, Rows: {len(df)}")
    
    if country_data_frames:
        combined_df = pd.concat(country_data_frames)
        combined_df = combined_df.loc[:, ~combined_df.columns.str.contains('^Unnamed')]
        data_frames[f"df_{country}"] = combined_df
        
# filtering years 2016-2022 for all countries
def filter_2015(df):
    filter_condition = (df['Date (UTC)'].dt.year == 2015) & (df['Date (UTC)'] != '2015-12-31T23:00:00.000Z')
    filtered_df = df[~filter_condition]
    return filtered_df

# creating the dfs
if "df_Germany" in data_frames:
    DE_df = filter_2015(data_frames["df_Germany"][4:])
    # DE_df = DE_df[DE_df['Date (UTC)'].dt.floor('H').dt.minute == 0]
    DE_df = DE_df[DE_df['Date (UTC)'].dt.strftime("%M") == "00"]
    print(DE_df)
if "df_Denmark" in data_frames:
    DK2_df = filter_2015(data_frames["df_Denmark"][2:])
    
if "df_Poland" in data_frames:
    PL_df = filter_2015(data_frames["df_Poland"][2:])
    
if "df_Finland" in data_frames:
    FIN_df = filter_2015(data_frames["df_Finland"][2:])
    
if "df_Netherlands" in data_frames:
    NL_df = filter_2015(data_frames["df_Netherlands"][2:])
    
if "df_Belgium" in data_frames:
    BE_df = filter_2015(data_frames["df_Belgium"][2:])
    
if "df_France" in data_frames:
    FR_df = filter_2015(data_frames["df_France"][2:])
    
# DF_VRE_GENERATION_HIST

# Germany
df_DE_wind_onshore = DE_df['Wind onshore'].astype(float)
df_DE_wind_offshore = DE_df['Wind offshore'].astype(float)
df_DE_solar = DE_df['Solar'].astype(float)
df_DE_ResLoad = DE_df['Residual load'].astype(float)
df_DE_Load = DE_df['Load'].astype(float)

# Denmark
df_DK2_wind_onshore = DK2_df['Wind onshore'].astype(float)
df_DK2_wind_offshore = DK2_df['Wind offshore'].astype(float)
df_DK2_solar = DK2_df['Solar'].astype(float)
df_DK2_ResLoad = DK2_df['Residual load'].astype(float)
df_DK2_Load = DK2_df['Load'].astype(float)

# Poland
df_PL_wind_onshore = PL_df['Wind onshore'].astype(float)
# df_PL_wind_offshore = PL_df['Wind offshore']
df_PL_solar = PL_df['Solar'].astype(float)
df_PL_ResLoad = PL_df['Residual load'].astype(float)
df_PL_Load = PL_df['Load'].astype(float)

# Finland
df_FIN_wind_onshore = FIN_df['Wind onshore'].astype(float)
# df_FIN_wind_offshore = FIN_df['Wind offshore']
# df_FIN_solar = FIN_df['Solar']
df_FIN_ResLoad = FIN_df['Residual load'].astype(float)
df_FIN_Load = FIN_df['Load'].astype(float)

# Netherlands
df_NL_wind_onshore = NL_df['Wind onshore'].astype(float)
df_NL_wind_offshore = NL_df['Wind offshore'].astype(float)
df_NL_solar = NL_df['Solar'].astype(float)
df_NL_ResLoad = NL_df['Residual load'].astype(float)
df_NL_Load = NL_df['Load'].astype(float)

# Belgium
df_BE_wind_onshore = BE_df['Wind onshore'].astype(float)
df_BE_wind_offshore = BE_df['Wind offshore'].astype(float)
df_BE_solar = BE_df['Solar'].astype(float)
df_BE_ResLoad = BE_df['Residual load'].astype(float)
df_BE_Load = BE_df['Load'].astype(float)

# France
df_FR_wind_onshore = FR_df['Wind onshore'].astype(float)
# df_FR_wind_offshore = FR_df['Wind offshore']
df_FR_solar = FR_df['Solar'].astype(float)
df_FR_ResLoad = FR_df['Residual load'].astype(float)
df_FR_Load = FR_df['Load'].astype(float)

# COVE CALC
start_year_indexes = [0, 8785, 17545, 26305, 35065, 43849, 52608]
year_labels = [2016, 2017, 2018, 2019, 2020, 2021, 2022]

def calculate_demand(load_df, start_index, end_index):
    load_data = load_df.astype(float).iloc[start_index:end_index]
    avg_load = load_data.mean()
    demand = load_data / avg_load
    return demand, avg_load


# Plotting Demands: 
def plot_demands(dfL, dfL_name, avg_load, start_indexes, year_labels):
    x = range(len(dfL))
    y = dfL.values.flatten()
    if len(y) == 0:
        print(f"No data available for {dfL_name}")
        return
    avg_load=dfL.mean()
    plt.scatter(x, y, marker='o', s=0.2, color='darkgreen')
    plt.axhline(y=avg_load, color='red', linestyle='--')
    plt.xticks(start_indexes, year_labels, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Normalized Hourly Demand')
    plt.title(f'Demand for {dfL_name}')
    plt.ylim(min(y), max(y))
    # plt.show()

# select start and end year: choose index
i_st_y=4
i_end_y=5

# Germany
df_DE_Load = df_DE_Load.astype(float)
D_DE, avg_D_DE = calculate_demand(df_DE_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_DE, 'D_DE (Germany)', avg_D_DE, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Denmark
df_DK2_Load = df_DK2_Load.astype(float)
D_DK2, avg_D_DK2 = calculate_demand(df_DK2_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_DK2, 'D_DK2 (Denmark)', avg_D_DK2, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Poland
df_PL_Load = df_PL_Load.astype(float)
D_PL, avg_D_PL = calculate_demand(df_PL_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_PL, 'D_PL (Poland)', avg_D_PL, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Finland
df_FIN_Load = df_FIN_Load.astype(float)
D_FIN, avg_D_FIN = calculate_demand(df_FIN_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_FIN, 'D_FIN (Finland)', avg_D_FIN, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Netherlands
df_NL_Load = df_NL_Load.astype(float)
D_NL, avg_D_NL = calculate_demand(df_NL_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_NL, 'D_NL (Netherlands)', avg_D_NL, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Belgium
df_BE_Load = df_BE_Load.astype(float)
D_BE, avg_D_BE = calculate_demand(df_BE_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_BE, 'D_BE (Belgium)', avg_D_BE, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# France
df_FR_Load = df_FR_Load.astype(float)
D_FR, avg_D_FR = calculate_demand(df_FR_Load, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_demands(D_FR, 'D_FR (France)', avg_D_FR, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])


# Data for SP for each country
df_FR_histSP = FR_df['Day Ahead Auction (FR)']
df_FIN_histSP = FIN_df['Day Ahead Auction (FI)']
df_BE_histSP = BE_df['Day Ahead Auction (BE)']
df_NL_histSP = NL_df['Day Ahead Auction (NL)']
df_DE_histSP = DE_df['Day Ahead Auction (DE-AT-LU)']
df_DK2_histSP = DK2_df['Day Ahead Auction (DK2)']
df_PL_histSP = PL_df['Day Ahead Auction (PL)']

def calculate_SP(SP_df, start_index, end_index):
    SP_data = SP_df.astype(float).iloc[start_index:end_index]
    avg_SP = SP_data.mean()
    norm_p = SP_data / avg_SP
    return norm_p, avg_SP

def plot_prices(SP_df, SP_name, avg_load, start_indexes, year_labels):
    x = range(len(SP_df))
    y = SP_df.values.flatten()
    valid_values = np.isfinite(y)  # Filter out NaN and Inf values
    y = y[valid_values]
    x = np.array(x)[valid_values]

    if len(y) == 0:
        print(f"No data available for {SP_name}")
        return

    avg_load = SP_df.mean()
    plt.scatter(x, y, marker='o', s=0.2, color='darkblue')
    plt.axhline(y=avg_load, color='red', linestyle='--')
    plt.xticks(start_indexes, year_labels, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Normalized Hourly Spot Prices')
    plt.title(f'Non-dim Spot prices for {SP_name}')
    plt.ylim(min(y), max(y))
    # plt.show()


# Germany
df_DE_histSP = df_DE_histSP.astype(float)
SP_DE, avg_SP_DE = calculate_SP(df_DE_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_DE, 'SP_DE (Germany)', avg_SP_DE, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Denmark
df_DK2_histSP = df_DK2_histSP.astype(float)
SP_DK2, avg_SP_DK2 = calculate_SP(df_DK2_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_DK2, 'SP_DK2 (Denmark)', avg_SP_DK2, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Poland
df_PL_histSP = df_PL_histSP.astype(float)
SP_PL, avg_SP_PL = calculate_SP(df_PL_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_PL, 'SP_PL (Poland)', avg_SP_PL, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Finland
df_FIN_histSP = df_FIN_histSP.astype(float)
SP_FIN, avg_SP_FIN = calculate_SP(df_FIN_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_FIN, 'SP_FIN (Finland)', avg_SP_FIN, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Netherlands
df_NL_histSP = df_NL_histSP.astype(float)
SP_NL, avg_SP_NL = calculate_SP(df_NL_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_NL, 'SP_NL (Netherlands)', avg_SP_NL, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# Belgium
df_BE_histSP = df_BE_histSP.astype(float)
SP_BE, avg_SP_BE = calculate_SP(df_BE_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_BE, 'SP_BE (Belgium)', avg_SP_BE, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# France
df_FR_histSP = df_FR_histSP.astype(float)
SP_FR, avg_SP_FR = calculate_SP(df_FR_histSP, start_year_indexes[i_st_y], start_year_indexes[i_end_y])
plot_prices(SP_FR, 'SP_FR (France)', avg_SP_FR, start_year_indexes[i_st_y:i_end_y], year_labels[i_st_y:i_end_y])

# m
# choose the country:

# --------------------------------------------------------------------------------------------------------------------------
# select start and end year: choose index
i_st_y=0
i_end_y=1
# --------------------------------------------------------------------------------------------------------------------------
data = {
    'NL': (D_NL, SP_NL),
    'DK2': (D_DK2, SP_DK2),
    'BE': (D_BE, SP_BE),
    'FR': (D_FR, SP_FR),
    'DE': (D_DE, SP_DE),
    'FIN': (D_FIN, SP_FIN),
    'PL': (D_PL, SP_PL),
}

slopes = {}
intercepts = {}
correlations = {}

for country, (D, SP) in data.items():

    nan_mask = np.isnan(D) | np.isnan(SP)

    D_no_nan = D[~nan_mask]
    SP_no_nan = SP[~nan_mask]

    m, n = np.polyfit(D_no_nan, SP_no_nan, 1)

    correlation = np.corrcoef(D, SP)[0, 1]

    slopes[f"m_{country}_{i_st_y}_{i_end_y}"] = m
    intercepts[f"n_{country}_{i_st_y}_{i_end_y}"] = n
    correlations[f"corr_{country}_{i_st_y}_{i_end_y}"] = correlation

    line = f'y = {m:.2f}x + {n:.2f}'

    plt.scatter(D, SP, color='blue', label='Data', s=0.2)
    plt.plot(D, m * D + n, color='red', label=line)
    plt.xlabel('D')
    plt.ylabel('SP')
    plt.title(f'Linear Relationship - {country}')
    plt.legend()
    plt.show()

slopes_df = pd.DataFrame.from_dict(slopes, orient='index', columns=['Slope'])
intercepts_df = pd.DataFrame.from_dict(intercepts, orient='index', columns=['Intercept'])
correlations_df = pd.DataFrame.from_dict(correlations, orient='index', columns=['Correlation'])

# Print the slopes, intercepts, and correlations for all countries
for country in data:
    print(f'Country: {country}')
    print('Slope (m):', slopes[f"m_{country}_{i_st_y}_{i_end_y}"])
    print('Intercept (n):', intercepts[f"n_{country}_{i_st_y}_{i_end_y}"])
    print('Correlation:', correlations[f"corr_{country}_{i_st_y}_{i_end_y}"])
    print()

# easy:
VRE_DE = df_DE_solar + df_DE_wind_offshore + df_DE_wind_onshore
VRE_DK2 = df_DK2_solar + df_DK2_wind_offshore + df_DK2_wind_onshore
VRE_FR = df_FR_solar + df_FR_wind_onshore
VRE_NL = df_NL_solar + df_NL_wind_offshore + df_NL_wind_onshore
VRE_FIN = df_FIN_wind_onshore
VRE_PL = df_PL_solar + df_PL_wind_onshore
VRE_BE= df_BE_solar +df_BE_wind_offshore+df_BE_wind_onshore

Q_BE= (VRE_BE/avg_D_BE)
Q_DE= VRE_DE/avg_D_DE
Q_DK2= VRE_DK2/avg_D_DK2
Q_FR= VRE_FR/avg_D_FR
Q_NL= VRE_NL/avg_D_NL
Q_FIN= VRE_FIN/avg_D_FIN
Q_PL= VRE_NL/avg_D_PL

Q_p_BE = Q_BE - Q_BE.mean()
Q_p_DE = Q_DE - Q_DE.mean()
Q_p_DK2 = Q_DK2 - Q_DK2.mean()
Q_p_FR = Q_FR - Q_FR.mean()
Q_p_NL = Q_NL - Q_NL.mean()
Q_p_FIN = Q_FIN - Q_FIN.mean()
Q_p_PL = Q_PL - Q_PL.mean()

# # p
# from automatized version:
# start_year_indexes = [0, 8785, 17545, 26305, 35065, 43849, 52608]
# year_labels = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
m_slope = slopes_df['Slope']
p_ratios = {}

for country in slopes_df.index:
    p_ratio = m_slope[country] * D_NL + (1 - m_slope[country]) - m_slope[country] * Q_p_NL.iloc[i_st_y:i_end_y]
    p_ratios[country] = p_ratio
    
    # Scatter plot
    plt.figure()
    plt.scatter(range(len(p_ratio)), p_ratio, s=0.5)
    plt.xlabel('Index: years')
    plt.ylabel('p_ratio vals')
    plt.title(f'p_ratio with {country}')
    
plt.show()

# Access the p_ratio values for each country
for country, p_ratio in p_ratios.items():
    print(f'{country} p_ratio_{i_st_y}_{i_end_y}:')
    print(p_ratio)
    print()
    