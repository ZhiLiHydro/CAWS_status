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
        '05536890']
stationName = ['Lake Michigan at Chicago Lock', 
        'Chicago River at Chicago Lock', 
        'Chicago River at Columbus Dr', 
        'Chicago River at Grand Ave', 
        'CSSC at Western Ave',
        'CSSC at Stickney, IL',
        'CSSC near Lemont, IL']

df = hf.NWIS(stationNum, 'iv', period='P7D', parameterCd='00065').get_data().df()

for i in range(7):
    df.rename(columns={df.columns[i*2]: stationName[i]}, inplace=True)

df['CSSC near Lemont, IL'] -= 27.431

df.to_csv('df.csv', float_format='%.2f', na_rep='nan')
ax = df.plot(linewidth=.5, marker='o', markersize=.5, figsize=(9,6))
ax.grid(color='grey', linestyle=':')
plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=3, bbox_to_anchor=(1.04,0.5), loc='center left')
plt.ylabel('Gage height in feet (Chicago City Datum)')
plt.title('Updated at ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
plt.tight_layout()
plt.savefig('./gauge.png')
plt.close()


