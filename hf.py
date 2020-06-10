from datetime import datetime
import hydrofunctions as hf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


stationNum = ['04087440', ## 1
        '05536121',       ## 2
        '05536123',       ## 3
        '05536118',       ## 4
        '05536137',       ## 5
        '05536140',       ## 6
        '05536890',       ## 7
        '05536290',       ## 8
        '05536995']       ## 9
stationName = ['Lake Michigan at Chicago Lock', ## 1
        'Chicago River at Chicago Lock',        ## 2
        'Chicago River at Columbus Dr',         ## 3
        'Chicago River at Grand Ave',           ## 4
        'Chicago Sanitary and Ship Canal (CSSC) at Western Ave', ## 5
        'CSSC at Stickney, IL',                 ## 6
        'CSSC near Lemont, IL',                 ## 7
        'Little Calumet River at South Holland, IL', ## 8
        'CSSC at Romeoville, IL']               ## 9
df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00065').get_data().df()
for i, n in enumerate(stationNum):
    df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
    df.rename(columns={'USGS:' + n + ':00065:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
    if 'Lemont' in stationName[stationNum.index(n)] or 'Romeoville' in stationName[stationNum.index(n)]:
        df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 27.431
    if 'Little Calumet' in stationName[stationNum.index(n)]:
        df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 4.48
df.to_csv('gauge-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
color = np.append(plt.cm.Dark2(np.linspace(0, 1, 8)), [[0, 0, 0, 1]], axis=0)
ax = df.plot(linewidth=.75, marker='o', markersize=.75, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Gage height, feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('gauge-IL.png', dpi=150)
plt.close()




stationNum = ['05536357', '04092750', '04092677']
stationName = ['Grand Calumet River at Hohman Ave at Hammond, IN', 
        'Indiana Harbor Canal at East Chicago, IN',
        'Grand Calumet River at Industrial Hwy at Gary, IN']
df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00065').get_data().df()
for i, n in enumerate(stationNum):
    df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
    df.rename(columns={'USGS:' + n + ':00065:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
    if 'Hammond' in stationName[stationNum.index(n)]:
        df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 4.48
    if 'Indiana Harbor' in stationName[stationNum.index(n)]:
        df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 9.28
    if 'Gary' in stationName[stationNum.index(n)]:
        df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] += 0.55
df.to_csv('gauge-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.75, marker='o', markersize=.75, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Gage height, feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('gauge-IN.png', dpi=150)
plt.close()




stationNum = ['05536890',
        '05536290', 
        '05533600', 
        '05537980', 
        '05536085', 
        '05536580',
        '05536500',
        '05536340']
stationName = ['CSSC near Lemont, IL', 
        'Little Calumet River at South Holland, IL',
        'Des Plaines River near Lemont, IL',
        'Des Plaines River at Route 53 at Joliet, IL',
        'North Branch Chicago River at N Pulaski Rd',
        'Stony Creek (west) near Worth, IL',
        'Tinley Creek near Palos Park, IL',
        'Midlothian Creek at Oak Forest, IL']
df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00060').get_data().df()
for i, n in enumerate(stationNum):
    df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
    df.rename(columns={'USGS:' + n + ':00060:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
df[df < 0] = np.nan
df.to_csv('discharge-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.75, marker='o', markersize=.75, figsize=(8,7), logy=True)
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Discharge, cubic feet per second')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('discharge-IL.png', dpi=150)
plt.close()




stationNum = ['05536357', '04092750', '04092677']
stationName = ['Grand Calumet River at Hohman Ave at Hammond, IN',
        'Indiana Harbor Canal at East Chicago, IN',
        'Grand Calumet River at Industrial Hwy at Gary, IN']
df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00060').get_data().df()
for i, n in enumerate(stationNum):
    df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
    df.rename(columns={'USGS:' + n + ':00060:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
df.to_csv('discharge-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.75, marker='o', markersize=.75, figsize=(8,7))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
plt.ylabel('Discharge, cubic feet per second')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
plt.tight_layout()
plt.savefig('discharge-IN.png', dpi=150)
plt.close()


