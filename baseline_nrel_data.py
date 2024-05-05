# BASELINE DATA ANALYSIS
# Started 5/4/2024
# Written by Julia Ehlers

"""
This file uses NREL's ResStock dataset to determine what the average size, age, and structure of the US
residential building set looks like. The results of the data were used to determine what type of energy
model was used for each location tested in my project.

in.geometry_foundation_type	string	n/a	Type of dwelling unit foundation
Ambient|Heated Basement|Slab|Unheated Basement|Unvented Crawlspace|Vented Crawlspace

"""

import pandas as pd
import math

df = pd.read_parquet('baseline.parquet')

relevant_input_columns = [
    'in.ashrae_iecc_climate_zone_2004',
    'in.state',
    'in.geometry_building_type_acs',
    'in.geometry_foundation_type'
]

relevant_data = df.loc[: , relevant_input_columns]
relevant_data = relevant_data.loc[relevant_data['in.geometry_building_type_acs'] == 'Single-Family Detached']

print("Florida:")
fl_data_state = relevant_data.loc[relevant_data['in.state'] == 'FL']
fl_data = fl_data_state.loc[fl_data_state['in.ashrae_iecc_climate_zone_2004'] == '1A']
print(fl_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Texas:")
tx_data_state = relevant_data.loc[relevant_data['in.state'] == 'TX']
tx_data = tx_data_state.loc[tx_data_state['in.ashrae_iecc_climate_zone_2004'] == '2A']
print(tx_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Arizona:")
az_data_state = relevant_data.loc[relevant_data['in.state'] == 'AZ']
az_data = az_data_state.loc[az_data_state['in.ashrae_iecc_climate_zone_2004'] == '2B']
print(az_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("North Carolina:")
nc_data_state = relevant_data.loc[relevant_data['in.state'] == 'NC']
nc_data = nc_data_state.loc[nc_data_state['in.ashrae_iecc_climate_zone_2004'] == '3A']
print(nc_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("California:")
ca_data_state = relevant_data.loc[relevant_data['in.state'] == 'CA']
ca_data = ca_data_state.loc[ca_data_state['in.ashrae_iecc_climate_zone_2004'] == '3C']
print(ca_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Washington:")
wa_data_state = relevant_data.loc[relevant_data['in.state'] == 'WA']
wa_data = wa_data_state.loc[wa_data_state['in.ashrae_iecc_climate_zone_2004'] == '4C']
print(wa_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Massachusetts:")
ma_data_state = relevant_data.loc[relevant_data['in.state'] == 'MA']
ma_data = ma_data_state.loc[ma_data_state['in.ashrae_iecc_climate_zone_2004'] == '5A']
print(ma_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Nebraska:")
ne_data_state = relevant_data.loc[relevant_data['in.state'] == 'NE']
ne_data = ne_data_state.loc[ne_data_state['in.ashrae_iecc_climate_zone_2004'] == '5A']
print(ne_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

print("Minnesota:")
mn_data_state = relevant_data.loc[relevant_data['in.state'] == 'MN']
mn_data = mn_data_state.loc[mn_data_state['in.ashrae_iecc_climate_zone_2004'] == '6A']
print(mn_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)



"""
MY CITY STATS:
IECC CZ label --> 1A, 2A, 2B, 3A, 3C, 4C, 5A, 6A
city label --> Miami, San Antonio, Phoenix, Charlotte, San Jose, Seattle, Boston, Omaha, Minneapolis
state label --> FL, TX, AZ, NC, CA, WA, MA, NE, MN
Average sq footage for that climate zone in each state
Percentage of single family homes that have low-e windows (for that CZ and state)

RELEVANT DATA:
Filter with: in.geometry_building_type_acs --> "Single-Family Detached"
Relevant categories:
    in.ashrae_iecc_climate_zone_2004 --> 1A, 2A, 2B, 3A, 3C, 4C, 5A, 6A
    in.state --> FL, TX, AZ, NC, CA, WA, MA, NE, MN
    in.geometry_foundation_type
    in.insulation_foundation_wall
    in.insulation_roof
    in.insulation_slab
    in.insulation_wall
    in.sqft
    in.windows

"""