import read
from collections import Counter
data = read.load_data()

data_headlines = data["headline"]
string_headlines = ""
for string in data_headlines:
    string_headlines+=str(string)+" "
split_lowered = string_headlines.lower().split(' ')

common = Counter(split_lowered).most_common(100)  
print(common)