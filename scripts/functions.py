import os
import arcpy
import local_vars


def select_trs_by_county(county_name):

	#make a layer from the feature class of the input county selection
	arcpy.MakeFeatureLayer_management(local_vars.counties, 'county_selection', '"County_NAME"' + '=' + "'"+ county_name + "'")

	#make a layer for the TRS feature
	arcpy.MakeFeatureLayer_management(local_vars.TRS_squares, 'TRS_All')

	#select features that intersect with the county selection layer
	arcpy.SelectLayerByLocation_management('TRS_All', 'INTERSECT', 'county_selection')

	#copy selected features to new feature class
	#arcpy.CopyFeatures_management('TRS_All', os.path.join(local_vars.temp, 'TRS_subset'))

	#return TRS IDs as list
	return field_2_list('TRS_All', 'FRSTDIVID')


def field_2_list(table, field):
	with arcpy.da.SearchCursor(table, [field]) as cursor:
		return sorted({row[0] for row in cursor})



