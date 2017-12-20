import pandas as pd
data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]

all_enrollment = data["total_enrollment"].sum()

columns = [
    "SCH_ENR_HI_M",
    "SCH_ENR_HI_F",
    "SCH_ENR_AM_M",
    "SCH_ENR_AM_F",
    "SCH_ENR_AS_M",
    "SCH_ENR_AS_F",
    "SCH_ENR_HP_M",
    "SCH_ENR_HP_F",
    "SCH_ENR_BL_M",
    "SCH_ENR_BL_F",
    "SCH_ENR_WH_M",
    "SCH_ENR_WH_F",
    "SCH_ENR_TR_M",
    "SCH_ENR_TR_F"
]

genders = ["TOT_ENR_M", "TOT_ENR_F"]
percentages = {}
for col in columns:
    percentages[col] =100*data[col].sum()/all_enrollment
    
genderpercentages = {}
for col in genders:
    genderpercentages[col] =100*data[col].sum()/all_enrollment

print("______________________")
print(percentages)
print("______________________")
print(genderpercentages)

