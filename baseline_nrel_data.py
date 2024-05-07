# BASELINE DATA ANALYSIS
# Started 5/4/2024
# Written by Julia Ehlers

"""
This file uses NREL's ResStock dataset to determine some basic statistics on the characteristics of the US
residential building stock. The results of the data were used to determine the baseline model for my project.

"""

import pandas as pd

def parse_by_state_iecc_cz(df, state = str, iecc_cz = str):
    
    # Allows user to sort out data for relevant state and IECC climate zone within that state.

    state_df = df.loc[df['in.state'] == state]
    state_df = state_df.loc[state_df['in.ashrae_iecc_climate_zone_2004'] == iecc_cz]

    return state_df

def make_stats_csv(df, col_name = str, csv_file_name = str):

    # Finds the number of occurences of each value in a column; normalized by total number of entries.
    # Uses this dataframe to print a .csv file with statistics.

    new_df = df[col_name].value_counts(normalize = True).to_frame()
    new_df.to_csv(csv_file_name)

    return f"{csv_file_name} PRINTED AS CSV."

def main():

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
    relevant_data = df.loc[: , relevant_input_columns]

    # Filter out everything other than single-family detached dwelling units.
    relevant_data = relevant_data.loc[relevant_data['in.geometry_building_type_acs'] == 'Single-Family Detached']

    # Delete data that is not from Nebraska or IECC CZ 5A and create a new dataframe.
    ne_data = parse_by_state_iecc_cz(relevant_data, "NE", "5A")
    
    # Find statistics about Nebraska stock from NREL dataset and print as .csv file.
    make_stats_csv(ne_data, "in.geometry_foundation_type", "ne_found_type_stats")
    make_stats_csv(ne_data, "in.windows", "ne_window_stats")
    make_stats_csv(ne_data, "in.sqft", "ne_sq_footage_stats")
    make_stats_csv(ne_data, "in.vintage", "ne_unit_age_stats")
    make_stats_csv(ne_data, "in.infiltration", "ne_ach50_val_stats")
    make_stats_csv(ne_data, "in.insulation_wall", "ne_wall_ins_stats")
    make_stats_csv(ne_data, "in.insulation_roof", "ne_roof_ins_stats")
    make_stats_csv(ne_data, "in.insulation_foundation_wall", "ne_found_ins_stats")
    make_stats_csv(ne_data, "in.insulation_slab", "ne_slab_ins_stats")
    

    """
    MY CITY STATS:
    IECC CZ label --> 1A, 2A, 2B, 3A, 3C, 4C, 5A, 6A
    city label --> Miami, San Antonio, Phoenix, Charlotte, San Jose, Seattle, Boston, Omaha, Minneapolis
    state label --> FL, TX, AZ, NC, CA, WA, MA, NE, MN
    Average sq footage for that climate zone in each state
    Percentage of single family homes that have low-e windows (for that CZ and state)
    
    """

if __name__ == '__main__':
    main()
