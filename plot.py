import pandas as pd
import os
import matplotlib.pyplot as plt

datafile="data/142273-test7-3.txt"
df0=pd.read_table(datafile,sep=' ')
cnames = []
for i in range(len(df0.columns)):
    cnames.append('u%d' % i)

todrop=cnames[5:]
cnames[0] = 't'
cnames[1] = 'm1'
cnames[2] = 'm2'
cnames[3] = 'm3'
cnames[4] = 'm4'

offsetdata={
    't' : 0,
    'm1': -162.4625,
    'm2': -153.9269,
    'm3': -156.6478,
    'm4': -163.86620,
    }
LO_RES = 0.0001
mresdata = {
    't' : 1,
    'm1': LO_RES,
    'm2': LO_RES,
    'm3': LO_RES,
    'm4': LO_RES,    
    }
df0.columns=cnames
df0.drop(columns=todrop, inplace=True)

mres = pd.Series(mresdata)
df1=df0*mres
df2 = df1+offsetdata

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(df2.t,df2.m1,'r.', label="m1",linestyle='dashed')
ax.plot(df2.t,df2.m2,'b.', label="m2",linestyle='dashed')
ax.plot(df2.t,df2.m3,'g.', label="m3",linestyle='dashed')
ax.plot(df2.t,df2.m4,'y.', label="m4",linestyle='dashed')
ax.minorticks_on()
ax.set_xlabel("Time [s]")
ax.set_ylabel("Position [mm]")
ax.set_title("plot: plot.py datafile: {datafile}".format(
    datafile=datafile))
ax.grid(b=True,which='both')
ax.grid(which='minor',linestyle='dotted')
ax.legend(loc='best')
plt.show()
