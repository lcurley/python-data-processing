import pandas as pd

sheet1 = pd.read_csv("CTOPP_SSRT_1TP_hand.csv")
sheet2 = pd.read_csv("PLING_Behavior_CANTAB_SWM.csv")

merged = sheet1.merge(sheet2, on='VisitID', how="outer")

merged.to_csv("PLING_TBSS_CTOPP_SSRT_SWM_1TP_handedness.csv")