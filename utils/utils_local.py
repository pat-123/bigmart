from utils import *

#-----------------specific
def plot_rides(sub_data,title_='scatterplot'):
    plt.scatter(sub_data.mahattan_dis, sub_data.fare_amount,label='distance')
    plt.scatter(sub_data.passenger_count, sub_data.fare_amount,color='red',label='passenger_count')
    plt.legend()
    plt.ylabel('fare')
    plt.title(title_)
    plt.show()

def variation(high_fare,txt):
    plotno=321
    plt.figure(figsize=(15,11))
    plt.subplot(plotno)
    plt.title(txt)
    var = '_%s'%plotno
    high_fare.groupby('passenger_count').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plotno+=1
    plt.subplot(plotno)
    high_fare.groupby('year').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plotno+=1
    plt.subplot(plotno)
    var = high_fare.groupby('month').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plotno+=1
    plt.subplot(plotno)
    high_fare.groupby('day').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plotno+=1
    plt.subplot(plotno)
    high_fare.groupby('time').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plotno+=1
    plt.subplot(plotno)
    high_fare.groupby('season').fare_amount.mean().plot.bar()
    plt.ylabel('average fare')
    plt.show()

    
def plot_rides_time(data,date_=False,hour_=False):
    hour = []
    fare=[]
    date =[]
    for i in range(len(data)):
        if date_:
            date.append(data.pickup_datetime.iloc[i].date())
        else:
            hour.append(data.pickup_datetime.iloc[i].hour)
        fare.append(data.fare_amount.iloc[i])
    if hour_:
        plt.scatter(hour,fare)
        plt.xlabel('pickup hour')
    else:
        plt.scatter(date,fare)
        plt.xlabel('pickup year')
    plt.ylabel('fare')
    
