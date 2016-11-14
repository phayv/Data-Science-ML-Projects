import time
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

######################################################## PIPELINE - START
f = open('api_key.txt','r')
api_key = f.read()

def Quandl_Data(stock_name):
   
    try:
        # getting pandas dataframes of values
        revenue    = quandl.get("RAYMOND/"+stock_name+"_TOTAL_REVENUE_A", authtoken=api_key)
        net_income = quandl.get("RAYMOND/"+stock_name+"_NET_INCOME_A", authtoken=api_key)
        APIC       = quandl.get("RAYMOND/"+stock_name+"_ADDITIONAL_PAID_IN_CAPITAL_A", authtoken = api_key)
        
        # make everything relative to millions and make arrays for values
        revenue_values    = np.array(revenue['Value']/1000000)
        revenue_dates     = np.array(revenue.index)
        net_income_values = np.array(net_income['Value']/1000000)
        net_income_dates  = np.array(revenue.index)
        APIC_values       = np.array(revenue['Value']/1000000)
        APIC_dates        = np.array(revenue.index)
                
        # plots, we share axes values because sometimes there are more or less data in different datasets
        fig = plt.figure(figsize = (12,10))

        ax1 = plt.subplot2grid((12,10),(0,0), rowspan = 3, colspan = 9)
        ax1.plot(revenue_dates,revenue_values)
        plt.xlabel('dates')
        plt.ylabel('revenue')
        
        ax2 = plt.subplot2grid((12,10),(4,0), rowspan = 3, colspan = 9, sharex = ax1)
        ax2.plot(net_income_dates,net_income_values)
        plt.xlabel('dates')
        plt.ylabel('net_income')
        
        ax3 = plt.subplot2grid((12,10),(8,0), rowspan = 3, colspan = 9, sharex = ax1)
        ax3.plot(APIC_dates,APIC_values)
        plt.xlabel('dates')
        plt.ylabel('APIC')
        
        plt.show()
    
    except Exception,e:
        print 'failed in the main loop',str(e)
        pass

    


######################################################## PIPELINE - END

Quandl_Data('ADBE')














