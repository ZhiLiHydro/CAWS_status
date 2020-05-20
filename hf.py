from datetime import datetime
import hydrofunctions as hf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


stationNum = ['04087440', 
        '05536121', 
        '05536123', 
        '05536118', 
        '05536137',
        '05536140', 
        '05536890',
        '05536290',
        '05536995']
stationName = ['Lake Michigan at Chicago Lock', 
        'Chicago River at Chicago Lock', 
        'Chicago River at Columbus Dr', 
        'Chicago River at Grand Ave', 
        'Chicago Sanitary and Ship Canal (CSSC) at Western Ave',
        'CSSC at Stickney, IL',
        'CSSC near Lemont, IL',
        'Little Calumet River at South Holland, IL',
        'CSSC at Romeoville, IL']
df = hf.NWIS(stationNum, 'iv', period='P7D', parameterCd='00065').get_data().df()
for n in stationNum:
    df.rename(columns={'USGS:' + n + ':00065:00000': stationName[stationNum.index(n)]}, inplace=True)
df['CSSC near Lemont, IL'] -= 27.431
df['Little Calumet River at South Holland, IL'] -= 4.48
df['CSSC at Romeoville, IL'] -= 27.431
df.to_csv('gauge-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.5, marker='o', markersize=.5, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Gage height in feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('gauge-IL.png', dpi=150)
plt.close()




stationNum = ['05536357', '04092750', '04092677']
stationName = ['Grand Calumet River at Hohman Ave at Hammond, IN', 
        'Indiana Harbor Canal at East Chicago, IN',
        'Grand Calumet River at Industrial Hwy at Gary, IN']
df = hf.NWIS(stationNum, 'iv', period='P7D', parameterCd='00065').get_data().df()
for n in stationNum:
    df.rename(columns={'USGS:' + n + ':00065:00000': stationName[stationNum.index(n)]}, inplace=True)
df['Grand Calumet River at Hohman Ave at Hammond, IN'] -= 4.48
df['Indiana Harbor Canal at East Chicago, IN'] -= 9.28
df['Grand Calumet River at Industrial Hwy at Gary, IN'] += 0.55
df.to_csv('gauge-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.5, marker='o', markersize=.5, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Gage height in feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('gauge-IN.png', dpi=150)
plt.close()




stationNum = ['05536890', '05536290', '05533600', '05537980']
stationName = ['CSSC near Lemont, IL',
        'Little Calumet River at South Holland, IL',
        'Des Plaines River near Lemont, IL',
        'Des Plaines River at Route 53 at Joliet, IL']
df = hf.NWIS(stationNum, 'iv', period='P7D', parameterCd='00060').get_data().df()
for n in stationNum:
    df.rename(columns={'USGS:' + n + ':00060:00000': stationName[stationNum.index(n)]}, inplace=True)
df.to_csv('discharge-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.5, marker='o', markersize=.5, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Discharge in cubic feet per second')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('discharge-IL.png', dpi=150)
plt.close()




stationNum = ['05536357', '04092750', '04092677']
stationName = ['Grand Calumet River at Hohman Ave at Hammond, IN',
        'Indiana Harbor Canal at East Chicago, IN',
        'Grand Calumet River at Industrial Hwy at Gary, IN']
df = hf.NWIS(stationNum, 'iv', period='P7D', parameterCd='00060').get_data().df()
for n in stationNum:
    df.rename(columns={'USGS:' + n + ':00060:00000': stationName[stationNum.index(n)]}, inplace=True)
df['Grand Calumet River at Hohman Ave at Hammond, IN'] -= 4.48
df['Indiana Harbor Canal at East Chicago, IN'] -= 9.28
df['Grand Calumet River at Industrial Hwy at Gary, IN'] += 0.459
df.to_csv('discharge-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.5, marker='o', markersize=.5, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Discharge in cubic feet per second')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('discharge-IN.png', dpi=150)
plt.close()


