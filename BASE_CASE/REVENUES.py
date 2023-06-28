# REVENUES
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = os.path.dirname(os.path.abspath(__file__))
# Read and convert to datetime the CSV generation files
# df_P_100 = pd.read_csv("P_w_100.csv")
df_P_100 = pd.read_csv(os.path.join(file_path, "P_100.csv"))
df_P_150 = pd.read_csv(os.path.join(file_path,"P_150.csv"))
df_P_PV = pd.read_csv(os.path.join(file_path,"P_PV.csv"))

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
#  in case:
tech = ['100', '150']
CorRES_loc = ['1', '2', '3', '4_1', '5_1', '6', '7', '8_1', '9', '10']
SP_loc = ['DE4-S', 'DE4-N', 'PL', 'FIN', 'NL', 'BE', 'DK2']
R_sc = ['R1', 'R4', 'R19']
year_sc = ['2025', '2035', '2045']
file_path = os.path.dirname(os.path.abspath(__file__))

# Definir las hojas de Excel y las columnas a extraer
sheets_to_read = ['2025', '2035', '2045']

columns_to_extract = ['Time (UTC)', 'BE', 'NL', 'FR', 'PL', 'FIN', 'DK2', 'DE4-S', 'DE4-N', 'DE4-W']

file_names = ['R1.xlsx', 'R4.xlsx', 'R19.xlsx']

dataframes = {}

for file_name in file_names:
    file_full_path = os.path.join(file_path, file_name)
    df = pd.read_excel(file_full_path, sheet_name=sheets_to_read, usecols=columns_to_extract)
    # df = pd.read_excel(file_name, sheet_name=None)
    # Crear un diccionario para almacenar los DataFrames por hoja
    dataframes[file_name] = df
    df_dict = {}
    
    # Leer las hojas de Excel y extraer las columnas necesarias
    for sheet_name in sheets_to_read:
        df_sheet = df[sheet_name][columns_to_extract]
        df_dict[sheet_name] = df_sheet
    
    # Agregar el diccionario de DataFrames al diccionario principal
    dataframes[file_name] = df_dict

# Acceder a los DataFrames según el archivo y la hoja
# for file_name, df_dict in dataframes.items():
#     for sheet_name, df_sheet in df_dict.items():
#         df_name = f"df_{file_name.split('.')[0]}_{sheet_name}"
#         globals()[df_name] = df_sheet  # Guardar el DataFrame en una variable con nombre dinámico
for file_name, df in dataframes.items():
    for sheet_name, df_sheet in df.items():
        df_name = f"df_{file_name.split('.')[0]}_{sheet_name}"
        globals()[df_name] = df_sheet  

# Imprimir los nombres de los DataFrames creados
print("DataFrames creados:")
for file_name in file_names:
    for sheet_name in sheets_to_read:
        df_name = f"df_{file_name.split('.')[0]}_{sheet_name}"
        df = globals()[df_name]  # Obtener el DataFrame
        
        # plt.plot(df['Time (UTC)'], df['BE'], label='BE')
        # plt.plot(df['Time (UTC)'], df['NL'], label='NL')
        # plt.plot(df['Time (UTC)'], df['FR'], label='FR')
        # plt.plot(df['Time (UTC)'], df['PL'], label='PL')
        # plt.plot(df['Time (UTC)'], df['FIN'], label='FIN')
        # plt.plot(df['Time (UTC)'], df['DK2'], label='DK2')
        # plt.plot(df['Time (UTC)'], df['DE4-S'], label='DE4-S')
        # plt.plot(df['Time (UTC)'], df['DE4-N'], label='DE4-N')
        # plt.plot(df['Time (UTC)'], df['DE4-W'], label='DE4-W')
        
        # plt.xlabel('Time (UTC)')
        # plt.ylabel('Eur/Mwh')
        # plt.title(f'Spot Prices for {df_name}')
        # plt.legend()
        # plt.show()
        
        
#  FOR TECH 100: annual revenues
revenues_R1_2045 = {
    'rev_100_1_R1_2045': [3032158.012025],
    'rev_100_2_R1_2045': [3662970.194675],
    'rev_100_3_R1_2045': [2434277.73124501],
    'rev_100_4_1_R1_2045': [3951263.83877999],
    'rev_100_5_1_R1_2045': [4521456.540055],
    'rev_100_6_R1_2045': [3256795.211895],
    'rev_100_7_R1_2045': [3680807.83065001],
    'rev_100_8_1_R1_2045': [4682683.41007001],
    'rev_100_9_R1_2045': [1515617.74481],
    'rev_100_10_R1_2045': [1988666.29824]
}


revenues_R1_2035 = {
    'rev_100_1_R1_2035': [4011733.53810999],
    'rev_100_2_R1_2035': [4576604.50007499],
    'rev_100_3_R1_2035': [3063761.654145],
    'rev_100_4_1_R1_2035': [4912544.21500501],
    'rev_100_5_1_R1_2035': [5878943.16382],
    'rev_100_6_R1_2035': [4459907.24709],
    'rev_100_7_R1_2035': [4667166.83166999],
    'rev_100_8_1_R1_2035': [5925534.31087501],
    'rev_100_9_R1_2035': [1980594.75391],
    'rev_100_10_R1_2035': [2495823.34485]
}


revenues_R1_2025 = {
    'rev_100_1_R1_2025': [4830472.82790001],
    'rev_100_2_R1_2025': [6235999.20916004],
    'rev_100_3_R1_2025': [4377567.68021502],
    'rev_100_4_1_R1_2025': [5804632.27262499],
    'rev_100_5_1_R1_2025': [8605491.403525],
    'rev_100_6_R1_2025': [5944574.667235],
    'rev_100_7_R1_2025': [6322893.17763],
    'rev_100_8_1_R1_2025': [7885506.80771504],
    'rev_100_9_R1_2025': [2474088.77672999],
    'rev_100_10_R1_2025': [3576006.36501499]
}

# for lifetime revenues
disc_rate = 0.05
lf_1 = np.array(range(0, 8))
annual_rev_lf1 = {}
rev_lf1_loc = {}

for loc in CorRES_loc:
    first_sec_lf1 = np.zeros(8)
    
    for year in lf_1:
        if year < len(lf_1):
            first_sec_lf_discounted = revenues_R1_2025['rev_100_' + loc + '_R1_2025'][0] / (1 + disc_rate) ** year
        else:
            first_sec_lf_discounted = revenues_R1_2025['rev_100_' + loc + '_R1_2025'][0]
        
        first_sec_lf1[year] = first_sec_lf_discounted
    annual_rev_lf1[loc] = first_sec_lf1
    rev_lf1 = np.sum(first_sec_lf1)
    rev_lf1_loc[loc] = rev_lf1

print(rev_lf1_loc)
# ----------------------------------------
lf_2 = np.array(range(8, 17))
annual_rev_lf2 = {}
rev_lf2_loc = {}

for loc in CorRES_loc:
    second_sec_lf2 = np.zeros(9)
    
    for year in lf_2:
        if year < len(lf_2):
            second_sec_lf_discounted = revenues_R1_2035['rev_100_' + loc + '_R1_2035'][0] / (1 + disc_rate) ** year
        else:
            second_sec_lf_discounted = revenues_R1_2035['rev_100_' + loc + '_R1_2035'][0]
        
        second_sec_lf2[year - lf_2[0]] = second_sec_lf_discounted
    annual_rev_lf2[loc] = second_sec_lf2
    rev_lf2 = np.sum(second_sec_lf2)
    rev_lf2_loc[loc] = rev_lf2

print(rev_lf2_loc)
# ----------------------------------------
lf_3 = np.array(range(17, 26))
annual_rev_lf3 = {}
rev_lf3_loc = {}

for loc in CorRES_loc:
    third_sec_lf3 = np.zeros(9)
    
    for year in lf_3:
        if year < len(lf_3):
            third_sec_lf_discounted = revenues_R1_2045['rev_100_' + loc + '_R1_2045'][0] / (1 + disc_rate) ** year
        else:
            third_sec_lf_discounted = revenues_R1_2045['rev_100_' + loc + '_R1_2045'][0]
        
        third_sec_lf3[year - lf_3[0]] = third_sec_lf_discounted
    annual_rev_lf3[loc] = third_sec_lf3
    rev_lf3 = np.sum(third_sec_lf3)
    rev_lf3_loc[loc] = rev_lf3

print(rev_lf3_loc)

rev_lifetime_loc = {}

for loc in CorRES_loc:
    rev_lifetime_loc[loc] = rev_lf1_loc[loc] + rev_lf2_loc[loc] + rev_lf3_loc[loc]
# print(rev_lifetime_loc)
print('IT WORKS')    
 
 
# dics created: 
dict_rev_100_lf1 = {
    '1': [32781392.296112426],
    '2': [42319819.139235966],
    '3': [29707808.850318592],
    '4_1': [39392402.036617614],
    '5_1': [58400077.932415515],
    '6': [40342103.3805671],
    '7': [42909514.0552548],
    '8_1': [53513993.62487476],
    '9': [16790090.257200293],
    '10': [24268114.4644621]
}

dict_rev_100_lf2 = {
    '1': [34809167.473443374],
    '2': [39710462.07068829],
    '3': [26583767.71655946],
    '4_1': [42625357.01246179],
    '5_1': [51010645.45096284],
    '6': [38697898.75254751],
    '7': [40496256.874188885],
    '8_1': [51414909.34965181],
    '9': [17185302.520953808],
    '10': [21655858.239264578]
}

dict_rev_100_lf3 = {
    '1': [27289422.108225],
    '2': [32966731.752074998],
    '3': [21908499.581205092],
    '4_1': [35561374.54901991],
    '5_1': [40693108.860495],
    '6': [29311156.907055],
    '7': [33127270.47585009],
    '8_1': [42144150.69063009],
    '9': [13640559.70329],
    '10': [17897996.684159998]
}

dic_rev_100_tot = {
    '1': [94879981.87778081],
    '2': [114997012.96199925],
    '3': [78200076.14808315],
    '4_1': [117579133.59809932],
    '5_1': [150103832.24387336],
    '6': [108351159.04016961],
    '7': [116533041.40529378],
    '8_1': [147073053.66515666],
    '9': [47615952.481444106],
    '10': [63821969.38788667]
}

   
