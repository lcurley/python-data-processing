# read in all files in directory
# merge all files on VisitID
# take only first timepoint for each subject
# remove rows with missing behavioral data
    
import glob
import pandas as pd
# import numpy as np

# directory = Documents/Python/virtual_env/PLING\TBSS/
# read in all files in directory
file_names = []
for files in glob.glob("*.csv"):
    file_names.append(files) # this works
   
# this seems to work, but depends on the files being the the same order every time
# 
count = 0 
for name in file_names:
	if count == 3:
		fivecRT_auto = pd.read_csv(name)
	if count == 4:
		bse_auto = pd.read_csv(name)
	if count == 5:
		ctopp_auto = pd.read_csv(name)
	if count == 6:
		rvp_auto = pd.read_csv(name)
	elif count == 7:
		ssrt_auto = pd.read_csv(name)
	count = count + 1
	
################################################################

goodImaging = pd.read_csv("PLING_TBSS_DiscMR750_SubjList_011415_no_duplicates.csv")
fivecRT = pd.read_csv("TBSS_5cRT.csv")
rvp = pd.read_csv("TBSS_RVP.csv")
ssrt = pd.read_csv("TBSS_SSRT.csv")
bse = pd.read_csv("TBSS_BSE.csv")
ctopp = pd.read_csv("TBSS_CTOPP.csv")

# drop rows with missing data
	# BEH_CANTAB_SWM_Between_errors
	# BEH_CANTAB_SST_SSRT_last_half
	# BEH_CANTAB_RVP_A
	# BEH_CANTAB_RTI_Five_choice_reaction_time
	# BEH_CTOPP_BW_Raw
	# BEH_EHI_Handedness

merged1 = goodImaging.merge(fivecRT, on='VisitID', how="outer")
f = merged1.dropna(subset= ['BEH_CANTAB_RTI_Five_choice_reaction_time'])
# f2 = merged1.dropna(subset= ['BEH_EHI_Handedness'])

merged2 = goodImaging.merge(rvp, on='VisitID', how="outer")
r = merged2.dropna(subset= ['BEH_CANTAB_RVP_A'])
# r2 = merged2.dropna(subset= ['BEH_EHI_Handedness'])

merged3 = goodImaging.merge(ssrt, on='VisitID', how="outer")
s = merged3.dropna(subset= ['BEH_CANTAB_SST_SSRT_last_half'])
# s2 = merged3.dropna(subset= ['BEH_EHI_Handedness'])

merged4 = goodImaging.merge(bse, on='VisitID', how="outer")
b = merged4.dropna(subset= ['BEH_CANTAB_SWM_Between_errors'])
# b2 = merged4.dropna(subset= ['BEH_EHI_Handedness'])

merged5 = goodImaging.merge(ctopp, on='VisitID', how="outer")
c = merged5.dropna(subset= ['BEH_CTOPP_BW_Raw'])
# c2 = merged5.dropna(subset= ['BEH_EHI_Handedness'])

# remove extra rows at the end of the worksheet
# df.dropna(subset = ['SubjID'])

################################################################	

# write filtered data to file

f.to_csv("singleTP_fivecRT_goodIM.csv")
r.to_csv("singleTP_RVP_goodIM.csv")
s.to_csv("singleTP_SSRT_goodIM.csv")
b.to_csv("singleTP_BSE_goodIM.csv")
c.to_csv("singleTP_CTOPP_goodIM.csv")

# f.to_csv("singleTP_noNA_fivecRT_goodIM.csv")
# r.to_csv("singleTP_noNA_RVP_goodIM.csv")
# s.to_csv("singleTP_noNA_SSRT_goodIM.csv")
# b.to_csv("singleTP_noNA_BSE_goodIM.csv")
# c.to_csv("singleTP_noNA_CTOPP_goodIM.csv")
