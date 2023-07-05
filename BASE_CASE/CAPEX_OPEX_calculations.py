# CAPEX and OPEX calculations
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np

# EUR/MW: RES. PAPER
# capex onshore= Wind Turbine Capex/Total CAPEX = 70.4% - (CAPEX 2025)
# capex offshore= Wind Turbine Capex/TOtal CAPEx= 33.6%
capex_turbineSP335HH100= 1140000 #EUR
capex_turbineSP335HH150= 1490000
capex_turbineSP277HH100= 1250000
capex_turbineSP277HH150= 1600000
capex_turbineSP198HH100= 1520000
capex_turbineSP198HH150= 1910000

dolltoeur= 0.92 
cap_inst= 50
# updated 2021 Cost of wind energy review:

capex_on_wf_SP335HH100= (capex_turbineSP335HH100/0.704)*cap_inst
capex_on_wf_SP335HH150= (capex_turbineSP335HH150/0.704)*cap_inst

capex_on_wf_SP277HH100= (capex_turbineSP277HH100/0.704)*cap_inst
capex_on_wf_SP277HH150= (capex_turbineSP277HH150/0.704)*cap_inst

capex_on_wf_SP199HH100= (capex_turbineSP198HH100/0.704)*cap_inst
capex_on_wf_SP199HH150= (capex_turbineSP198HH150/0.704)*cap_inst


# offshore: for locs 5.1 (NL) and 8.1 (DK2): locate it further away (match CAPEX & LOC) up to 50 m. Move into the sea.
# should be around 1.8 - 2 (but they are a bit hight)
# according to DEA: the relationship in % btw onshore, offshore and PV is described as follows: 
# units: EUR/MWh
# on= 1: CAPEX
off_perc_capex= 40.43/28.895
ns_perc_capex= 34.85/28.895
on_perc_capex= 28.895/28.895
pv_perc_capex= 30.24/28.895
# on= 1: OPEX
off_perc_opex= 16.878/6.227
ns_perc_opex= 17.37/6.227
on_perc_opex= 6.227/6.227
pv_perc_opex= 8.638/6.227
# this capex estimation is way too high. 
# if we follow the relationships from DEA techonology:

capex_ns_wf_SP335HH100= ns_perc_capex*capex_on_wf_SP335HH100
capex_ns_wf_SP335HH150= ns_perc_capex*capex_on_wf_SP335HH150
capex_off_wf_SP335HH100= off_perc_capex*capex_on_wf_SP335HH100
capex_off_wf_SP335HH150= off_perc_capex*capex_on_wf_SP335HH150

capex_pv_try_MW= pv_perc_capex*capex_turbineSP277HH100
capex_pv_try= capex_pv_try_MW*cap_inst
# 1,76 Meur/MW and 1,34 Meur/MW
# capex_pv= 30.24*(cap_inst * 8736) 
# capex_pv= 30.24*(AEP)
# $/MW from https://atb.nrel.gov/electricity/2021/commercial_pv
dolltoeur= 0.92 
capex_pv_low_MW= 1231378*dolltoeur
capex_pv_low= capex_pv_low_MW*cap_inst*dolltoeur
capex_pv_mod_MW= 1337338*dolltoeur
capex_pv_mod= capex_pv_mod_MW*cap_inst
capex_pv_high_MW= 1616351*dolltoeur
capex_pv_high= capex_pv_high_MW*cap_inst
#  VISUALIZATION

x_values = ['capex_ns_wf_SP335HH100', 'capex_ns_wf_SP335HH150', 'capex_off_wf_SP335HH100',
            'capex_off_wf_SP335HH150', 'capex_on_wf_SP277HH100', 'capex_on_wf_SP277HH150',
            'capex_on_wf_SP199HH100', 'capex_on_wf_SP199HH150', 'capex_on_wf_SP335HH100',
            'capex_on_wf_SP335HH150', 'capex_pv_try','capex_pv_low', 'capex_pv_high']
colors = ['darkblue' if 'off' in x else 'blue' if 'pv' not in x else 'orange' if 'pv' in x else 'brown' for x in x_values]
y_values = [capex_ns_wf_SP335HH100, capex_ns_wf_SP335HH150, capex_off_wf_SP335HH100,
            capex_off_wf_SP335HH150, capex_on_wf_SP277HH100, capex_on_wf_SP277HH150,
            capex_on_wf_SP199HH100, capex_on_wf_SP199HH150, capex_on_wf_SP335HH100,
            capex_on_wf_SP335HH150, capex_pv_try, capex_pv_low, capex_pv_high]

plt.gca().yaxis.set_major_formatter(lambda x, _: '{:.0f}e6'.format(x/1e6))
plt.bar(x_values, y_values, color= colors)
plt.xlabel('Capex for each wind tech')
plt.ylabel('MEUR')
plt.title('CAPEX for 50 MW wind farm')
plt.xticks(rotation=90)
plt.show()

# # FOLLOWING THE RELATIONSHIPS THE OPEX FOUND FOR EACH TECHNOLOGY IS:
# SOLAR
dolltoeur= 0.92 
opex_pv_low= 14205*dolltoeur*cap_inst # EUR/MW-year
opex_pv_high= 17355*dolltoeur*cap_inst # EUR/MW-year
opex_pv_mod= 15072*dolltoeur*cap_inst 

# ----------------
# WIND
opex_on_high=43000*dolltoeur*cap_inst
opex_on_low= 38298*dolltoeur*cap_inst
opex_on_mod=40791*dolltoeur*cap_inst

opex_off_high= 109405*dolltoeur*cap_inst
opex_off_low= 87437*dolltoeur*cap_inst
opex_off_mod= 94648*dolltoeur*cap_inst
#  VISUALIZATION

x_values = ['opex_off_high', 'opex_off_low', 'opex_off_mod',
            'opex_on_high', 'opex_on_low', 'opex_on_mod',
            'opex_pv_high', 'opex_pv_low', 'opex_pv_mod']

colors = ['darkblue' if 'off' in x else 'blue' if 'pv' not in x else 'orange' if 'pv' in x else 'brown' for x in x_values]

y_values = [opex_off_high, opex_off_low, opex_off_mod,
            opex_on_high, opex_on_low, opex_on_mod,
            opex_pv_high, opex_pv_low, opex_pv_mod]

plt.gca().yaxis.set_major_formatter(lambda x, _: '{:.0f}e6'.format(x/1e6))
plt.bar(x_values, y_values, color=colors)
plt.xlabel('Opex for each wind tech')
plt.ylabel('MEUR')
plt.title('OPEX for 50 MW wind farm')
plt.xticks(rotation=90)
plt.show()

print(opex_on_mod)