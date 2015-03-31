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


# to deal with optional inputs being skipped
def input_parameter(i):
	value = arcpy.GetParameterAsText(i)
	if value == '#' or value == '':
		value = None
	return value


# returns sorted list of values from an attribute table
def field_2_list(table, field):
	with arcpy.da.SearchCursor(table, [field]) as cursor:
		return sorted({row[0] for row in cursor})


# Creates a partial TRS match for use in a regular expression. Periods are wild character values
def partial_FID(trs_class):
	if trs_class.state is None:
		trs_class.state = '..'
	if trs_class.pm is None:
		trs_class.pm = '..'
	if trs_class.t is None:
		trs_class.t = '...'
	else:
		trs_class.t = check_length(trs_class.t, 3)
	if trs_class.t_frac is None:
		trs_class.t_frac = '.'
	if trs_class.t_dir is None:
		trs_class.t_dir = '.'
	if trs_class.r is None:
		trs_class.r = '...'
	else:
		trs_class.r = check_length(trs_class.r, 3)
	if trs_class.r_frac is None:
		trs_class.r_frac = '.'
	if trs_class.r_dir is None:
		trs_class.r_dir = '.'
	if trs_class.s is None:
		trs_class.s = '..'
	else:
		trs_class.s = check_length(trs_class.s, 2)

	# CA 14 008 0 S 022 0 W 0 SN 06 0 (example of FID format)
	wild = (trs_class.state + trs_class.pm + trs_class.t + trs_class.t_frac + trs_class.t_dir+ trs_class.r
	        + trs_class.r_frac + trs_class.r_dir + '...' + trs_class.s + '.')

	return wild.upper()


# returns list of TRS IDs that match the partial input using a regular expression match
def matches(partial_FID, FID_list):
	potential_matches = []
	for id in FID_list:
		match = re.search(partial_FID, id)
		if match:
			potential_matches.append(id)
	return potential_matches


# function that checks length of input and adds zeros if not right length for field
def check_length(class_elm, field_length):
	if len(class_elm) == field_length:
		return class_elm
	elif len(class_elm) == field_length - 1:
		return '0' + class_elm
	elif len(class_elm) == field_length - 2:
		return '00' + class_elm
	else:
		print("Error: input length does not match field type")
		return '.' * field_length  # returns an empty string if length of class element is bigger than the field



def select_trs_by_county(county_name):
	# make a layer from the feature class of the input county selection
	arcpy.MakeFeatureLayer_management(local_vars.counties, 'county_selection', '"County_NAME"' + '=' + "'"+ county_name + "'")

	# make a layer for the TRS feature
	arcpy.MakeFeatureLayer_management(local_vars.PLSS_sections, 'TRS_All')

	# select features that intersect with the county selection layer
	arcpy.SelectLayerByLocation_management('TRS_All', 'INTERSECT', 'county_selection')

	# copy selected features to new feature class
	# arcpy.CopyFeatures_management('TRS_All', os.path.join(local_vars.temp, 'TRS_subset'))

	# return TRS IDs as list
	return field_2_list('TRS_All', local_vars.TRS_ID_fieldname)

