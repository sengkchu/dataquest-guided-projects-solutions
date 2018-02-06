f = open("AviationData.txt", "r")
reader = f.read()
aviation_data = reader.split("\n")

#Structure 1: Create a list of lists
aviation_list = [row.split(" | ") for row in aviation_data]


#Long method O(n**2) literates the 2 dimensionality of the list. Returns the row
lax_code = []
for i in range(len(aviation_list)):
    for j in range(len(aviation_list[i])):
        if aviation_list[i][j] == 'LAX94LA336':
            lax_code.append(aviation_list[i])
            
#Linear method O(n) that searches only the row
lax_code2= []
for row in aviation_list:
    if 'LAX94LA336' in row:
        lax_code2.append(row)

      


#Structure 2: Create a list of dictionaries
columns_names = aviation_data[0].split(" | ")
aviation_data_new = aviation_data[1:]

aviation_dict_list = []
for row in aviation_data_new:
    split = row.split(" | ")
    temp_dict = {}
    for i in range(len(split)):
        temp_dict[columns_names[i]] = split[i]
    aviation_dict_list.append(temp_dict)

#Using the list of dictionaries, search for LAX94LA336
lax_dict = []
for dictionary in aviation_dict_list:
    if "LAX94LA336" in dictionary.values():
        lax_dict.append(dictionary)
        

#The order of this search is linear O(n) because we still had to loop through the first list. However this is more efficient than looping two lists.


#Count how many accidents in U.S. State
#We'll use the list of dictionaries with keys = 'Country', 'Location'
#We'll have to create a new list named "state_accidents" to store each state name then count it using a counter
#The value for 'Location' is in the format of 'CITY, STATE'

from collections import Counter


state_accidents_list = []
for dictionary in aviation_dict_list:
    if 'Country' in dictionary:
        if dictionary['Country'] == 'United States':
            state_list = dictionary['Location'].split(", ")
            try:
                state = state_list[1]
            except:
                state = ""
            if len(state) == 2:
                state_accidents_list.append(state)
state_accidents = Counter(state_accidents_list)


#We want to know the monthly injuries in each unique month and year.
#Keys we'll need: 'Event Date' and extract the month number, 'Total Fatal Injuries' and 'Total Serious Injuries'.
#Event date are in the format of MM/DD/YYYY we'll need to convert this to MM/YYYY using .split("/") -> into a list like this ['MM', 'DD', 'YYYY']
#We'll then display this as a list of lists
month_names = []
for dictionary in aviation_dict_list:
    month_injuries = []
    if 'Event Date' in dictionary:
        split_date = dictionary['Event Date'].split('/')
        try:
            s_injuries = int(dictionary['Total Serious Injuries'])
        except:
            s_injuries = 0
        try:
            f_injuries = int(dictionary['Total Fatal Injuries'])
        except:
            f_injuries = 0
        try:
            MM_YYYY = split_date[0]+'/'+split_date[2]
        except:
            MM_YYYY = ""
        if len(MM_YYYY) == 7:
            month_injuries.append(MM_YYYY)
            month_injuries.append(s_injuries)
            month_injuries.append(f_injuries)
    month_names.append(month_injuries)  


#This list of lists contains a list for each accident that has occurred, we want to compact this list so it only shows each MM/YYYY once. A  way to do this is using a dictionary with MM/YYYY as keys then make another dictionary with Serious Injury and Fatal Injury as keys
monthly_injuries = {}
for accident in month_names:
    try:
        month = accident[0]
        s_injury = accident[1]
        f_injury = accident[2]
    except:
        continue
    if month not in monthly_injuries:
        monthly_injuries[month] = {'Serious Injury': s_injury, 'Fatal Injury': f_injury}
    if month in monthly_injuries:
        monthly_injuries[month]['Serious Injury'] += s_injury
        monthly_injuries[month]['Fatal Injury'] += f_injury

print(monthly_injuries)

#Now we have a dictionary of dictionaries with MM/YYYY as keys, and another dictionary assigned to each key with values for serious injuries and fatal injuries