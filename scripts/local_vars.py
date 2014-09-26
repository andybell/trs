import os

#set working directory to TRS directory
wd = r'C:\Users\ambell\Documents\TRS'

#file paths
counties = os.path.join(wd, r"data\geodata.gdb\CA_Counties")
PLSS_sections = os.path.join(wd, r"data\geodata.gdb\PLSSFirstDivision")
PLSS_township = os.path.join(wd, r"data\geodata.gdb\PLLSTownship")

# Field Name for unique ID
TRS_ID_fieldname = 'FRSTDIVID'

#temp_output
temp = os.path.join(wd, r"data\temp.gdb")