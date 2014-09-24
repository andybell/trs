import os

#set working directory to TRS directory
wd = os.path.dirname(os.getcwd())

#file paths
counties = os.path.join(wd, r"data\geodata.gdb\CA_Counties")
PLSS_sections = os.path.join(wd, r"data\geodata.gdb\PLSSFirstDivision")
PLSS_township = os.path.join(wd, r"data\geodata.gdb\PLLSTownship")


#temp_output
temp = os.path.join(wd, r"data\temp.gdb")
