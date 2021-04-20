# coding: utf-8
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import hydrofunctions as hf


def gageHeightIL():
    stationNum = ['04087440',
            '05536121',
            '05536123',
            '05536118',
            '05536137',
            '05536140',
            '05536890',
            #'05536290',
            '05536995']
    stationName = ['Lake Michigan at Chicago Lock',
            'Chicago River at Chicago Lock',
            'Chicago River at Columbus Dr',
            'Chicago River at Grand Ave',
            'Chicago Sanitary and Ship Canal (CSSC) at Western Ave',
            'CSSC at Stickney, IL',
            'CSSC near Lemont, IL',
            #'Little Calumet River at South Holland, IL',
            'CSSC at Romeoville, IL']
    df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00065').df()
    for i, n in enumerate(stationNum):
        df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
        df.rename(columns={'USGS:' + n + ':00065:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
        if 'Lemont' in stationName[stationNum.index(n)] or 'Romeoville' in stationName[stationNum.index(n)]:
            df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 27.431
        if 'Little Calumet' in stationName[stationNum.index(n)]:
            df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 4.48
    df.to_csv('./csv/gageHeight-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
    df.plot(linewidth=.75, marker='.', markersize=1, figsize=(8,7)).grid(color='grey', linestyle=':')
    plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
    plt.ylabel('Gage height, feet (Chicago City Datum)')
    plt.title('Updated ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
    plt.tight_layout()
    plt.savefig('./img/gageHeight-IL.png', dpi=150)
    plt.close()


def gageHeightIN():
    stationNum = ['05536356', '04092750', '04092677']
    stationName = ['Grand Calumet River at Columbia Ave at Hammond, IN', 
            'Indiana Harbor Canal at East Chicago, IN',
            'Grand Calumet River at Industrial Hwy at Gary, IN']
    df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00065').df()
    for i, n in enumerate(stationNum):
        df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
        df.rename(columns={'USGS:' + n + ':00065:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
        if 'Hammond' in stationName[stationNum.index(n)]:
            df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 5.13
        if 'Indiana Harbor' in stationName[stationNum.index(n)]:
            df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] -= 9.28
        if 'Gary' in stationName[stationNum.index(n)]:
            df['USGS ' + n + ': ' + stationName[stationNum.index(n)]] += 0.55
    df['USGS 04092750: Indiana Harbor Canal at East Chicago, IN (6-hour Mean)'] = savgol_filter(df['USGS 04092750: Indiana Harbor Canal at East Chicago, IN'], 73, 1, mode='nearest')
    df.to_csv('./csv/gageHeight-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
    df.plot(y=['USGS 04092750: Indiana Harbor Canal at East Chicago, IN',
               'USGS 04092750: Indiana Harbor Canal at East Chicago, IN (6-hour Mean)',
               'USGS 04092677: Grand Calumet River at Industrial Hwy at Gary, IN',
               'USGS 05536356: Grand Calumet River at Columbia Ave at Hammond, IN'],
            linewidth=.75, marker='.', markersize=1, figsize=(8,6),
            color=['lightgrey', 'tab:blue', 'tab:orange', 'tab:red']).grid(color='grey', linestyle=':')
    plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
    plt.ylabel('Gage height, feet (Chicago City Datum)')
    plt.title('Updated ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
    plt.tight_layout()
    plt.savefig('./img/gageHeight-IN.png', dpi=150)
    plt.close()


def dischargeIL():
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
    df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00060').df()
    for i, n in enumerate(stationNum):
        df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
        df.rename(columns={'USGS:' + n + ':00060:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
    df[df < 0] = np.nan
    df.to_csv('./csv/discharge-IL-dataframe.csv', float_format='%.2f', na_rep='nan')
    df.plot(linewidth=.75, marker='.', markersize=1, figsize=(8,7), logy=True).grid(color='grey', linestyle=':')
    plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
    plt.ylabel('Discharge, cubic feet per second')
    plt.title('Updated ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
    plt.tight_layout()
    plt.savefig('./img/discharge-IL.png', dpi=150)
    plt.close()


def dischargeIN():
    stationNum = ['04092750', '04092677']
    stationName = ['Indiana Harbor Canal at East Chicago, IN',
            'Grand Calumet River at Industrial Hwy at Gary, IN']
    df = hf.NWIS(stationNum, 'iv', period='P14D', parameterCd='00060').df()
    for i, n in enumerate(stationNum):
        df.drop(df.columns[2*(len(stationNum)-i)-1], axis=1, inplace=True)
        df.rename(columns={'USGS:' + n + ':00060:00000': 'USGS ' + n + ': ' + stationName[stationNum.index(n)]}, inplace=True)
    df['USGS 04092750: Indiana Harbor Canal at East Chicago, IN (6-hour Mean)'] = savgol_filter(df['USGS 04092750: Indiana Harbor Canal at East Chicago, IN'], 73, 1, mode='constant')
    df.to_csv('./csv/discharge-IN-dataframe.csv', float_format='%.2f', na_rep='nan')
    df.plot(y=['USGS 04092750: Indiana Harbor Canal at East Chicago, IN',
               'USGS 04092750: Indiana Harbor Canal at East Chicago, IN (6-hour Mean)',
               'USGS 04092677: Grand Calumet River at Industrial Hwy at Gary, IN'],
            linewidth=.75, marker='.', markersize=1, figsize=(8,6),
            color=['lightgrey', 'tab:blue', 'tab:red']).grid(color='grey', linestyle=':')
    plt.legend(edgecolor='black', facecolor='white', framealpha=1, markerscale=8, bbox_to_anchor=(.5,-.2), loc='upper center')
    plt.ylabel('Discharge, cubic feet per second')
    plt.title('Updated ' + datetime.now().strftime('%m/%d/%Y %H:%M:%S') + ' US Central Time')
    plt.tight_layout()
    plt.savefig('./img/discharge-IN.png', dpi=150)
    plt.close()


if __name__ == '__main__':
    plt.rcParams['font.family'] = 'Times New Roman'
    gageHeightIL()
    gageHeightIN()
    dischargeIL()
    dischargeIN()

