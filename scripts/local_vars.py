import os

#set working directory to TRS directory
wd = os.path.dirname(os.getcwd())

#file paths
counties = os.path.join(wd, "data\geodata.gdb\CA_Counties")
TRS_squares = os.path.join(wd, "data\geodata.gbd\PLSSFirstDivision")
