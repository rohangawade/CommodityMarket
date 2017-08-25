import pandas as pd
from datetime import datetime
import sys,getopt

def main(argv):
    if len(argv) == 0:
        print 'You must pass some parameters. Use \"-h\" to help.'
    if len(argv) == 1 and argv[0] == '-h': 
        print "\To use this we can pass follwing attribute\nStart Day & End date (in the format 2017-05-22) &commodity""" 
    start = argv[0]
    end = argv[1]
    commodity = argv[2]
    data = getCommodityPrice(start,end,commodity)
    print(data)

def getCommodityPrice(startdate,enddate,commodity):
    commodityfile = commodity+'.csv'
    df = pd.read_csv(commodityfile)
    df['Date']= pd.to_datetime(df['Date'])
    # df.head()
    startdate = datetime.strptime(startdate,'%Y-%m-%d')
    enddate = datetime.strptime(enddate,'%Y-%m-%d')
    # print(start)
    # print(end)
    mask = (df['Date'] <= startdate) & (df['Date'] > enddate)
    dfreq = (df.loc[mask])
    dfreq['Price']= dfreq.Price.astype(str).str.replace(',','')
    dfreq['Price'] = dfreq.Price.astype(float)
    # print(dfreq['Price'])
    ret_data = commodity +" "+str(dfreq['Price'].values.mean())+" "+str(dfreq['Price'].values.var())
    return ret_data
    
if __name__ == '__main__':
    main(sys.argv[1:])