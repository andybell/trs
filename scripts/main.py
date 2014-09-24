__author__ = 'ambell'
#import modules
#import arcpy
import os

import local_vars
from local_vars import *

import functions
from functions import *

state = arcpy.GetParameterAsText(0)
pm = arcpy.GetParameterAsText(1)
twnshp = arcpy.GetParameterAsText(2)
twnshp_frac = arcpy.GetParameterAsText(3)
twnshp_dir = arcpy.GetParameterAsText(4)
rangeship = arcpy.GetParameterAsText(5)
rangeship_frac = arcpy.GetParameterAsText(6)
rangeship_dir = arcpy.GetParameterAsText(7)

TRS_input = (state, pm, twnshp, twnshp_frac, twnshp_dir, rangeship, rangeship_frac, rangeship_dir)

arcpy.AddMessage(TRS_input)

all_tr = field_2_list(PLSS_township, 'PLSSID')

pFID = partial_FID(TRS_input)

arcpy.AddMessage(pFID)

match = matches(pFID, all_tr)

arcpy.AddMessage(match)

#Turns township file into feature layer for selection
arcpy.MakeFeatureLayer_management(PLSS_township, 'Township_lyr')

# for each potential match in match list -> add to selection
for m in match:
	arcpy.SelectLayerByAttribute_management('Township_lyr', 'ADD_TO_SELECTION', '"PLSSID"' + '=' + "'" + m + "'")

arcpy.CopyFeatures_management('Township_lyr', os.path.join(temp, "Selection"))

