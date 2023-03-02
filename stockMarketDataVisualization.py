
#This program creates a live store marker data visualization of any ticker the user selects
#It shows details of the high, low, open and closing prices of the ticker

import plotly.graph_objs as go
import yfinance

# to get data from API, arguments needed are ticker, start time and end time(period), and interval in order
# for time arguments 1 minute is 1m and 1 hour is 1h, 1d, 1wk and 1mo

# get user input to choose the ticker
ticker = input("Please enter ticker: ").upper()

#ask if user would like to modify period and interval
default_data = input("Would you like to modify the period and interval for the data? Yes or No (if no default data would be for a period of one 1 day and an interval of 1 minute) ").lower()
if default_data == 'yes':
    period = input("Enter your choice for period: \n m = minute \n h = hour \n d = day \n wk = week \n mo = month \n").lower()
    period_time = input("Enter amount of " + period + " : ")

    period_data = period_time + period

    interval = input("Enter your choice for interval: \n m = minute \n h = hour \n d = day \n wk = week \n mo = month \n").lower()
    interval_time = input("Enter amount of " + interval + " : ")

    interval_data = interval_time + interval

else:
    period_data = "1d"
    interval_data = "1m"

# get data from API
data = yfinance.download(tickers = ticker, period = period_data, interval = interval_data)

#create figure
fig = go.Figure()

#represen data as cadlesticks
fig.add_trace(go.Candlestick(x = data.index, open = data['Open'], close = data['Close'], high = data['High'], low = data['Low']))

#Titles
fig.update_layout(title=ticker + ' live share price data', yaxis_title='Stock Price (US per shares)')

#reset range selector
fig.update_xaxes(
    rangeselector = dict(buttons = list([dict(step = 'all')]))
)
#show figure
fig.show()
