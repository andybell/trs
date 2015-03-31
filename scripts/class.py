__author__ = 'ambell'


class TRSclass:
	"""class for township range section data with defaults set to None """""

	def __init__(self, state=None, county=None, pm=None, twnshp=None, twnshp_frac=None, twnshp_dir =None, rangeship=None, rangeship_frac=None, rangeship_dir=None, section_num=None):
		self.state = state
		self.county = county
		self.pm = pm
		self.twnshp = twnshp
		self.twnshp_frac = twnshp_frac
		self.twnshp_dir = twnshp_dir
		self.rangeship = rangeship
		self.rangeship_frac = rangeship_frac
		self.rangeship_dir = rangeship_dir
		self.section_num = section_num