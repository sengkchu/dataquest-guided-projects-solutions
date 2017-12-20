import read
data = read.load_data()

domains = data['url'].value_counts(sort = True, ascending = False)
domains = domains[0:99:] #shows 100 items
for name, row in domains.items():
    print("{0}: {1}".format(name, row))
    #if row == 10: #shows everything more than 10 submissions
        #break
    
