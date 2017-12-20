import read
import pandas as pd
import datetime
from dateutil.parser import parse
data = read.load_data()

def hour_extract(series):
    datetimeobj = parse(series)
    hour = datetimeobj.hour
    
    return hour



data['hour'] = data['submission_time'].apply(hour_extract)


hours = data['hour'].value_counts(sort = True, ascending = False)
#hours = hours[0:24:] #shows 24 hours
for name, value in hours.items():
    print("{0}: {1}".format(name, value))