__author__ = 'ambell'

import arcpy

state = arcpy.GetParameterAsText(0)
pm = arcpy.GetParameterAsText(1)
twnshp = arcpy.GetParameterAsText(2)
twnshp_frac = arcpy.GetParameterAsText(3)
twnshp_dir = arcpy.GetParameterAsText(4)
rangeship = arcpy.GetParameterAsText(5)
rangeship_frac = arcpy.GetParameterAsText(6)
rangeship_dir = arcpy.GetParameterAsText(7)

TRS_truple  = (state, pm, twnshp, twnshp_frac, twnshp_dir, rangeship, rangeship_frac, rangeship_dir)

arcpy.AddMessage(TRS_truple)

