import csv
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    with open(filename,"r") as f:
        data = list(csv.reader(f))
    data = np.array(data)[1:,:]
    return data

data = load_data("average_crimes_report.csv")
print(data)
changes_in_crime = []
with open("changes_in_crime.csv","w") as f:
    f.write("YearMonth,Change in crime\n")
    for i in range(1,40):
        changes_in_crime.append([i,float(data[i-1,1])-float(data[i,1])])
        f.write(data[i,0]+ ","+str(float(data[i-1,1])-float(data[i,1]))+"\n")
    f.close()
changes_in_crime = np.array(changes_in_crime)
plt.title("Changes in Crime Boston")
plt.xlabel('Months from Aug 2015 to Sept 2018')
plt.ylabel('Change in Number of Crimes')
plt.plot(changes_in_crime[:,0],changes_in_crime[:,1])
plt.show()
