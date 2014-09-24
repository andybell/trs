__author__ = 'ambell'

#import modules
import arcpy
import os

#file paths
trs = "some_string"

counties = r"county_path"

TRS_squares = r"trs_squares"



# parse trs inputs into categories



# Select TRS_squares that are in correct county
# Not sure if all data records will have county info so make this optional
# quick way to subset TRS to search for match

def selectbycounty(county_name):
	#select county that matches input county name
	arcpy.SelectLayerByAttribute_management()
	#select
	arcpy.SelectLayerByLocation_management(TRS_squares, "INTERSECT")


# Search TRS_squares (either full or subset from county selection) for partial match with input trs data
# Need to include matching with partial or incomplete data - ie flag with errors
# create error list for multiple partial matches (ie same trs from multiple meridians)


