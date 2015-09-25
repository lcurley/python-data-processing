import pandas as pd

ctopp = pd.read_csv("PLING_TBSS_CTOPP.csv")
ssrt = pd.read_csv("PLING_TBSS_SSRT.csv")

merged = ctopp.merge(ssrt, on='VisitID', how="outer")

merged.to_csv("PLING_TBSS_CTOPP_SSRT_merged.csv")