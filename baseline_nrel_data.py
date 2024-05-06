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
    'in.vintage',
    'in.sqft',
    'in.geometry_building_type_acs',
    'in.geometry_foundation_type',
    'in.infiltration',
    'in.insulation_foundation_wall',
    'in.insulation_roof',
    'in.insulation_slab',
    'in.insulation_wall',
    'in.windows'
]

# Eliminate extra columns from .parquet data file to make it easier to work with.
# I also chose to work with single family dwelling units only, so I filtered out everything else.
relevant_data = df.loc[: , relevant_input_columns]
relevant_data = relevant_data.loc[relevant_data['in.geometry_building_type_acs'] == 'Single-Family Detached']

# Everything in the quotes comment below was from when I intended to check multiple locations. I decided to focus on
# Nebraska, but didn't want to delete it, so I reccommend collapsing the comment for easy viewing.

"""
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

print("Minnesota:")
mn_data_state = relevant_data.loc[relevant_data['in.state'] == 'MN']
mn_data = mn_data_state.loc[mn_data_state['in.ashrae_iecc_climate_zone_2004'] == '6A']
print(mn_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)

"""

# Delete data that is not from Nebraska or IECC CZ 5A and create a new dataframe.
ne_data_state = relevant_data.loc[relevant_data['in.state'] == 'NE']
ne_data = ne_data_state.loc[ne_data_state['in.ashrae_iecc_climate_zone_2004'] == '5A']

# Print uselful statistics on NE housing stock (topic in first line of each chunk).
print("Basement Types:")
print(ne_data['in.geometry_foundation_type'].value_counts(normalize = True) * 100)
print("\n")

print("Window Types:")
print(ne_data['in.windows'].value_counts(normalize = True) * 100)
print("\n")

print("Size in Square Feet:")
print(ne_data['in.sqft'].value_counts(normalize = True) * 100)
print("\n")

print("Age of Dwelling Units:")
print(ne_data['in.vintage'].value_counts(normalize = True) * 100)
print("\n")

print("ACH50 Values:")
print(ne_data['in.infiltration'].value_counts(normalize = True) * 100)
print("\n")

print("Wall Insulation:")
print(ne_data['in.insulation_wall'].value_counts(normalize = True) * 100)
print("\n")

print("Roof Insulation:")
print(ne_data['in.insulation_roof'].value_counts(normalize = True) * 100)
print("\n")

print("Foundation Wall Insulation:")
print(ne_data['in.insulation_foundation_wall'].value_counts(normalize = True) * 100)
print("\n")

print("Slab Insulation:")
print(ne_data['in.insulation_slab'].value_counts(normalize = True) * 100)
print("\n")


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