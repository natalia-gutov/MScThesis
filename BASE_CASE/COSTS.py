# COSTS
# Adding a comment.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Read and convert to datetime the CSV generation files
df_P_100 = pd.read_csv("P_100.csv")
df_P_150 = pd.read_csv("P_150.csv")
df_P_PV = pd.read_csv("P_PV.csv")

df_P_100['time'] = pd.to_datetime(df_P_100['time'], utc=True)
df_P_150['time'] = pd.to_datetime(df_P_150['time'], utc=True)
df_P_PV['time'] = pd.to_datetime(df_P_PV['time'], utc=True)

def filter_on_year(df: pd.DataFrame, year: int):
    """This functions filters a dataframe on a year using the utc_timestamp column.

    Args:
        year (int): year e.g. 2017
    Return:
        df: a dataframe filter on the year parameter
    """
    return df[df['time'].dt.year == year]

sel_year= 2012

# automatize for all dataframes
df_sel_year= filter_on_year(df=df_P_100, year=sel_year)

# COST CALCULATION
# inputs:
# capex = 92750000 #EUR

cap_inst = 50  # MW
capex = (1140000 * cap_inst)  # EUR/MW*MW
capex_wind_100= [1140000, 1250000, 1520000]*cap_inst #335-277-199
capex_wind_150= [1490000, 1600000, 1910000]*cap_inst #335-277-199
opex = 13720  # EUR/MWh

years = 25

WACC = 0.06  # A real WACC factors in inflation and is therefore lower, all other things being equal, than a nominal WACC which does not account for inflation.
OM_rate = 0.02

# procedure:
year_frac = np.array(range(years + 1))
disc_factor = [1 / ((1 + WACC) ** year_frac[i]) for i in range(years + 1)]

PVC = [capex, 0, opex]
OM_cost = opex * (1 + OM_rate)

for i in range(3, years):
    pvc_value = OM_cost * disc_factor[i]
    PVC.append(pvc_value)

NPC = sum(PVC)