__author__ = 'ambell'
#import modules
import arcpy
import os

import local_vars
from local_vars import *

import functions
from functions import *


#TODO: get parameters in a loop?
state = arcpy.GetParameterAsText(0)
pm = arcpy.GetParameterAsText(1)
twnshp = arcpy.GetParameterAsText(2)
twnshp_frac = arcpy.GetParameterAsText(3)
twnshp_dir = arcpy.GetParameterAsText(4)
rangeship = arcpy.GetParameterAsText(5)
rangeship_frac = arcpy.GetParameterAsText(6)
rangeship_dir = arcpy.GetParameterAsText(7)
section_num = arcpy.GetParameterAsText(8)

TRS_input = (state, pm, twnshp, twnshp_frac, twnshp_dir, rangeship, rangeship_frac, rangeship_dir, section_num)

"""
TRS_tester = ('CA', '', '039', '', 'N', '009', '', 'E', '35')
"""

arcpy.AddMessage(TRS_input)

all_tr = field_2_list(PLSS_sections, TRS_ID_fieldname)

pFID = partial_FID(TRS_input)

arcpy.AddMessage(pFID)

match = matches(pFID, all_tr)

arcpy.AddMessage("Number of Matches: %s" %len(match))
arcpy.AddMessage(match)

PLSS_file = arcpy.GetParameterAsText(9)

# for each potential match in match list -> add to selection
for m in match:
	arcpy.AddMessage("Adding %s to selection" %m)
	arcpy.SelectLayerByAttribute_management(PLSS_file, 'ADD_TO_SELECTION', '"' + TRS_ID_fieldname + '"' + '=' + "'" + m + "'")

mxd = arcpy.mapping.MapDocument('CURRENT')
arcpy.AddMessage(mxd)
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
arcpy.AddMessage(df)
df.zoomToSelectedFeatures()
arcpy.RefreshActiveView()


