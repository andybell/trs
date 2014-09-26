__author__ = 'ambell'
#import modules
from local_vars import *
from functions import *

try:

	# call TRS class for input parameters
	input_parameters = TRSclass(state=input_parameter(0), county=input_parameter(1),
	                      pm=input_parameter(2),t=input_parameter(3),
	                      t_dir=input_parameter(4), r=input_parameter(5),
	                      r_dir=input_parameter(6), s=input_parameter(7))


	arcpy.AddMessage("Creating wildcard search FID from inputs.....")

	pFID = partial_FID(input_parameters)

	arcpy.AddMessage("Wildcard: %s" %pFID)

	PLSS_file = arcpy.GetParameterAsText(8)


	#if county info available call select features to shorten list
	if input_parameters.county != None:
		county_sel = arcpy.SelectLayerByAttribute_management("CA_Counties", "NEW_SELECTION", '"County_NAME"' + '=' + "'"+ input_parameters.county + "'" )

		trs_sub = arcpy.SelectLayerByLocation_management(PLSS_file, 'INTERSECT', county_sel)

		trs_searchlist = field_2_list(trs_sub, TRS_ID_fieldname)

		#clears selections
		arcpy.SelectLayerByAttribute_management(PLSS_file, "CLEAR_SELECTION")
		arcpy.SelectLayerByAttribute_management("CA_Counties", "CLEAR_SELECTION")

	else:
		trs_searchlist = field_2_list(PLSS_sections, TRS_ID_fieldname)

	match = matches(pFID, trs_searchlist)

	arcpy.AddMessage("Number of Matches: %s" %len(match))
	arcpy.AddMessage(match)

	# for each potential match in match list -> add to selection
	for m in match:
		arcpy.AddMessage("Adding %s to selection" %m)
		arcpy.SelectLayerByAttribute_management(PLSS_file, 'ADD_TO_SELECTION', '"' + TRS_ID_fieldname + '"' + '=' + "'" + m + "'")

	mxd = arcpy.mapping.MapDocument('CURRENT')
	df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
	arcpy.AddMessage("Zooming to selection")
	df.zoomToSelectedFeatures()
	arcpy.RefreshActiveView()


except arcpy.ExecuteError:
	print arcpy.GetMessages()
