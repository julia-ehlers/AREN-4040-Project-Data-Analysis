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
