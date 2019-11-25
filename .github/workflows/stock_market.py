import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import os

# feed a stock list
get_stocks = ("WBC.AX")

# Get the data of the stock/s
weekly_data = yf.Ticker(get_stocks)

#print (weekly_data.history("5d"))
loop_rows = pd.DataFrame(weekly_data.history("5d"))

def main():
    print('The results for the stock', get_stocks)
    for index, row in loop_rows.iterrows():
        try:
            print ('The opening price was ', row['Open'], ' and the closing price was ', row['Close'])
            # representloss
            if row['Open'] > row['Close']:
                daily_loss = row['Open'] - row['Close']
                percentage_loss = (daily_loss/row['Open'] * 100)
                rounded_percentage_loss = round(percentage_loss, 2)
                print ('Loss for the day: ', rounded_percentage_loss, '%')
            # represent gain
            elif row['Open'] < row['Close']:
                daily_gain = row['Close'] - row['Open']
                percentage_gain = (daily_gain/row['Open'] * 100)
                rounded_percentage_gain = round(percentage_gain,2)
                print ('Gain for the day: ', rounded_percentage_gain, '%')
            # represent neither a loss nor gain
            else:
                print ("The stock gained 0 % for the day")
        except:
            break
    change_directory()

"""
Steps to do now
1. function that changes directotry
2. send everything to a text document
3. connect to email server
4. send email to myself
"""


def change_directory():
    write_to_directory = os.chdir()

if __name__ == "__main__":
    print ("This program calculates the movement of stocks for the previous 5 days")
    main()