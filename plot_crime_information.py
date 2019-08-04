import csv
import numpy as np
import matplotlib.pyplot as plt



def load_data(filename):
    with open(filename,"r") as f:
        data = list(csv.reader(f))
    data = np.array(data)[1:,:]
    return data

data = load_data("crime_report.csv")

districts = ['D14', 'C11', 'D4', 'B3', 'B2', 'C6', '' ,'A1', 'E5', 'A7', 'E13', 'E18', 'A15']
d14_report,c11_report, d4_report, b3_report, b2_report, c6_report, _report, a1_report, e5_report, a7_report, e13_report, e18_report, a15_report = [],[],[],[],[],[],[],[],[],[],[],[],[]

x = []

for i in range(40):
    x.append(i+1)
x = np.array(x)
for row in data:
    if row[0] == 'D14':
        d14_report.append([row[2]])
    elif row[0] == 'C11':
        c11_report.append([row[2]])
    elif row[0] == 'D4':
        d4_report.append([row[2]])
    elif row[0] == 'B3':
        b3_report.append([row[2]])
    elif row[0] == 'B2':
        b2_report.append([row[2]])
    elif row[0] == 'C6':
        c6_report.append([row[2]])
    elif row[0] == '':
        _report.append([row[2]])
    elif row[0] == 'A1':
        a1_report.append([row[2]])
    elif row[0] == 'E5':
        e5_report.append([row[2]])
    elif row[0] == 'A7':
        a7_report.append([row[2]])
    elif row[0] == 'E13':
        e13_report.append([row[2]])
    elif row[0] == 'E18':
        e18_report.append([row[2]])
    elif row[0] == 'A15':
        a15_report.append([row[2]])


d14_report.reverse()
c11_report.reverse()
d4_report.reverse()
b3_report.reverse()
b2_report.reverse()
c6_report.reverse()
_report.reverse()
a1_report.reverse()
e5_report.reverse()
a7_report.reverse()
e13_report.reverse()
e18_report.reverse()
a15_report.reverse()

d14_report = np.array(d14_report).astype(int)
c11_report = np.array(c11_report).astype(int)
d4_report = np.array(d4_report).astype(int)
b3_report = np.array(b3_report).astype(int)
b2_report = np.array(b2_report).astype(int)
c6_report = np.array(c6_report).astype(int)
_report = np.array(_report).astype(int)
a1_report = np.array(a1_report).astype(int)
e5_report = np.array(e5_report).astype(int)
a7_report = np.array(a7_report).astype(int)
e13_report = np.array(e13_report).astype(int)
e18_report = np.array(e18_report).astype(int)
a15_report = np.array(a15_report).astype(int)

mean_crime_report = np.zeros(d14_report.shape)

for i in range(d14_report.shape[0]):
    mean_crime_report[i] = float(e13_report[i] + e18_report[i] + a15_report[i]+d14_report[i] + c11_report[i] + d4_report[i] + b3_report[i] + b2_report[i] + c6_report[i] + _report[i] + a1_report[i] + e5_report[i] + a7_report[i])/13

plt.title("Crimes in Boston Per District")
plt.xlabel('Months from Aug 2015 to Sept 2018')
plt.ylabel('Number of Crimes')
plt.plot(x,d14_report,'-b',label='D14')
plt.plot(x,c11_report,'-g',label='C11')
plt.plot(x,d4_report,'-o',label='D4')
plt.plot(x,b3_report,'-r',label='B3')
plt.plot(x,b2_report,'-y',label='B2')
plt.plot(x,c6_report,'-k',label='C6')
plt.plot(x,_report,'--b',label= 'No Code')
plt.plot(x,a1_report,'--g',label='A1')
plt.plot(x,e5_report,'--o',label='E5')
plt.plot(x,a7_report,'--r',label='A7')
plt.plot(x,e13_report,'--y',label='E13')
plt.plot(x,e18_report,'--k',label='E18')
plt.plot(x,a15_report,'+b',label='A15')
plt.legend(title="District Codes",loc="upper left")
plt.show()

plt.title("Average Crimes In Boston Each Month")
plt.xlabel('Months from Aug 2015 to Sept 2018')
plt.ylabel('Number of Crimes')
plt.plot(x,mean_crime_report)
plt.show()

with open("average_crimes_report.csv","w") as f:
    f.write("YearMonth,Average Number of Crimes\n")
    for r in range(40):
        f.write(data[r][1]+","+str(mean_crime_report[r][0])+"\n")
    f.close()


