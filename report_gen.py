import csv
import numpy as np

def load_data(filename):
    with open(filename,"r") as f:
        data = list(csv.reader(f))
    data = np.array(data)
    return data[1:,:]


data = load_data("crime.csv")

districts = []

for row in data:
    if row[4] in districts:
        continue
    else:
        districts.append(row[4])

print(districts)

months = []
for row in data:
    if int(row[9]) >= 10:
        rec = int(row[8]+row[9])
    else:
        rec = int(row[8]+"0"+row[9])
    
    if rec in months:
        continue
    else:
        months.append(rec)

sorted(months,reverse=True)

"""

Districts: D14, C11, D4, B3, B2, C6, '' A1, E5, A7, E13, E18, A15

"""
crime_report = []

for district in districts:
    for month in months:
        crimes = 0
        for row in data:
            if int(row[9]) >= 10:
                rec = int(row[8]+row[9])
            else:
                rec = int(row[8]+"0"+row[9])
            if rec == month and row[4] == district:
                crimes += 1
        crime_report.append([district,month,crimes])
#crime_report = np.array(crime_report)
with open("crime_report.csv","w") as f:
    f.write("District Code, YearMonth, Number of Crimes\n")
    for row in crime_report:
        f.write(row[0]+","+str(row[1])+","+str(row[2])+"\n")
    f.close()

j = 0