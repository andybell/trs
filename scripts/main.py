__author__ = 'ambell'

#import modules
#import arcpy
import os

import local_vars
from local_vars import *

import functions
from functions import *


# Select TRS_squares that are in correct county
# Not sure if all data records will have county info so make this optional
# quick way to subset TRS to search for match
test = select_trs_by_county('Lake')

print test

# Search TRS_squares (either full or subset from county selection) for partial match with input trs data
# Need to include matching with partial or incomplete data - ie flag with errors
# create error list for multiple partial matches (ie same trs from multiple meridians)


