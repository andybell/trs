import os
import arcpy
import re
import local_vars

class TRSclass:
	"""class for township range section data with defaults set to None. t = township, r = range, s = section"""""

	def __init__(self, state=None, county=None, pm=None, t=None, t_frac=None, t_dir =None, r=None, r_frac=None, r_dir=None, s=None):
		self.state = state
		self.county = county
		self.pm = pm
		self.t = t
		self.t_frac = t_frac
		self.t_dir = t_dir
		self.r = r
		self.r_frac = r_frac
		self.r_dir = r_dir
		self.s = s


# returns sorted list of values from an attribute table
def field_2_list(table, field):
	with arcpy.da.SearchCursor(table, [field]) as cursor:
		return sorted({row[0] for row in cursor})


def partial_FID(trs_class):
	if trs_class.state is None:


#CA 14 008 0 S 022 0 W 0 SN 06 0


# Creates a partial TRS match for use in a regular expression. Periods are wild character values
def partial_FID(TRS_truple): #TRS_truple  = (state, pm, twnshp, twnshp_frac, twnshp_dir, rangeship, rangeship_frac, rangeship_dir, section_num)
	FID_template = '.'*20
	FID_list = list(FID_template)
	if TRS_truple[0] != '':
		FID_list[0:2] = TRS_truple[0]

	if TRS_truple[1] != '':
		FID_list[2:4] = TRS_truple[1]

	if TRS_truple[2] != '':
		FID_list[4:7] = TRS_truple[2]

	if TRS_truple[3] != '':
		FID_list[7:8] = TRS_truple[3]

	if TRS_truple[4] != '':
		FID_list[8:9] = TRS_truple[4]

	if TRS_truple[5] != '':
		FID_list[9:12] = TRS_truple[5]

	if TRS_truple[6] != '':
		FID_list[12:13] = TRS_truple[6]

	if TRS_truple[7] != '':
		FID_list[13:14] = TRS_truple[7]

	if TRS_truple[8] != '':
		FID_list[17:19] = TRS_truple[8]

	FID = "".join(FID_list)
	return FID

# returns list of TRS IDs that match the partial input using a regular expression match
def matches(partial_FID, FID_list):
	potential_matches = []
	for id in FID_list:
		match = re.search(partial_FID, id)
		if match:
			potential_matches.append(id)
	return potential_matches


#TODO: function that checks length of input and adds zeros if not right length for field


def select_trs_by_county(county_name):

	#make a layer from the feature class of the input county selection
	arcpy.MakeFeatureLayer_management(local_vars.counties, 'county_selection', '"County_NAME"' + '=' + "'"+ county_name + "'")

	#make a layer for the TRS feature
	arcpy.MakeFeatureLayer_management(local_vars.PLSS_sections, 'TRS_All')

	#select features that intersect with the county selection layer
	arcpy.SelectLayerByLocation_management('TRS_All', 'INTERSECT', 'county_selection')

	#copy selected features to new feature class
	#arcpy.CopyFeatures_management('TRS_All', os.path.join(local_vars.temp, 'TRS_subset'))

	#return TRS IDs as list
	return field_2_list('TRS_All', 'FRSTDIVID')