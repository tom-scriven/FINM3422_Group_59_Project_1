# Loading the yfinance API, to extract data from Yahoo Finance about Reliance Worldwide Corporation (RWC) and the ASX200 index.
# The data is downloaded for the period from January 1, 2016, to October 1, 2024.
import yfinance as yf
RWC = yf.download(tickers='RWC.AX', start='2016-01-01', end='2025-04-25')
print(RWC)

ASX200 = yf.download(tickers='^AXJO', start='2016-01-01', end='2025-04-25')
print(ASX200)

import pandas as pd
import matplotlib.pyplot as plt

# Import the CSV file of Historical Price Targets of RWC extracted from Bloomberg
price_targets = pd.read_csv("price_targets_converted.csv")
price_targets.columns = ['Year', 'Price Target'] 
price_targets['Year'] = pd.to_datetime(price_targets['Year'], format='%Y')

fig, ax1 = plt.subplots(figsize=(10, 5))

# Using the extracted data from the yfinance API, the RWC.AX close prices are plotted 
rwc_line = ax1.plot(RWC['Close'], label='RWC Price', color='blue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Price ($AUD)')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
# Using the extracted data from the yfinance API, the ASX200 close prices are plotted
asx200_line = ax2.plot(ASX200['Close'], label='ASX200 Price', color='green')
ax2.set_ylabel('Index Level (points)')
ax2.tick_params(axis='y')

# Using the extracted data from the CSV file, the price targets are plotted
#As the 2016 price target is not in the original data, it is added manually to the DataFrame
new__row = pd.DataFrame({'Year': [pd.Timestamp('2016')], 'Price Target': [3.00]})
price_targets = pd.concat([price_targets, new__row], ignore_index=True).sort_values(by='Year')

price_target_dots = ax1.scatter(price_targets['Year'], price_targets['Price Target'], 
                             label='Average Analyst Price Target', color='red', marker='o', s=50)
ax1.set_xlabel('Year')
ax1.set_ylabel('Price ($AUD)')
ax1.tick_params(axis='y')
ax1.set_ylim(0,6)

# Label the Price Target points accordingly
for x,y in zip(price_targets['Year'], price_targets['Price Target']):
    ax1.annotate(f'{y}', xy=(x, y), textcoords="offset points", xytext=(0,6),
                ha='center', fontsize=8, color='black')

# Label the lines and create a legend for the lines
lines = rwc_line + asx200_line + [price_target_dots]
plt.legend(lines, ['RWC.AX', 'ASX200', 'Price Targets'], loc='upper left')

plt.title('RWC Price vs ASX200 Price vs Average Analyst Price Target')
plt.show()