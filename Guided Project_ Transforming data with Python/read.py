import pandas as pd
from collections import Counter
def load_data():
    data = pd.read_csv('hn_stories.csv')
    data.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return data
