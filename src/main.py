import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm

from consts import * 


def load_data(path):
    """
    Load data from path
    
    param path : str
        Path to the file 

    return : pd.DataFrame
    """

    return pd.read_csv(path)


def plot_time_series(data, col_name, title=None, **kwargs):
    """
    Plot data

    param data : pd.DataFrame
        Data to plot
    """

    plt.plot(data[col_name], **kwargs)
    plt.xlabel('x')
    plt.ylabel('y')
    if title: 
        plt.title(title)
    plt.show()

electricity_data = load_data('data/electricity_prices_day_ahead_hourly_all.csv')

# Only take data from 01.01.2016 to 31.12.2017
electricity_data = electricity_data[0:17543]
monthly_data = electricity_data['fixing_i_volume'][0:SAMPLES_PER_MONTH]

# plot_time_series(electricity_data, 'fixing_i_volume')
plot_acf(monthly_data, lags=20, adjusted=True)
plot_pacf(monthly_data, lags=20)
result = sm.tsa.seasonal_decompose(monthly_data, period=SAMPLES_PER_DAY)
result.plot()
plt.show()



# # Dane dla jednego dnia 
# plot_time_series(electricity_data[0:SAMPLES_PER_DAY], 'fixing_i_volume', title='Dane dla jednego dnia')
# # Dane dla tygodnia 
# plot_time_series(electricity_data[0:SAMPLES_PER_WEEK], 'fixing_i_volume', title='Dane dla tygodnia')
# # Dane dla miesiąca
# plot_time_series(electricity_data[0:SAMPLES_PER_MONTH], 'fixing_i_volume', title='Dane dla miesiąca')
# # Dane dla roku
# plot_time_series(electricity_data[0:SAMPLES_PER_YEAR], 'fixing_i_volume', title='Dane dla roku')
