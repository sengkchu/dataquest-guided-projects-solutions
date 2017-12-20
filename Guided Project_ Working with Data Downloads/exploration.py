import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
value_counter = data["JJ"].value_counts()
value_counter2 = data["SCH_STATUS_MAGNET"].value_counts()
print(value_counter)
print("____________________________")
print(value_counter2)
print("____________________________")
pivoted1 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")

pivoted2 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")


print(pivoted1)
print("____________________________")
print(pivoted2)