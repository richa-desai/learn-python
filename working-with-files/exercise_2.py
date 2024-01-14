'''
stocks.csv contains stock price, earnings per share and book value.
You are writing a stock market application that will process this file and
create a new file with financial metrics such as pe ratio and price to book ratio.
These are calculated as,
pe ratio = price / earnings per share
price to book ratio = price / book value

Your input format (stocks.csv) is,
Company Name 	Price 	Earnings Per Share 	Book Value
Reliance 	1467 	66 	653
Tata Steel 	391 	89 	572

Output.csv should look like this,
Company Name 	PE Ratio 	PB Ratio
Reliance 	22.23 	2.25
Tata Steel 	4.39 	0.68
'''
import os
print(os.listdir())
dir1 = os.getcwd()
dir1 += '/working-with-files'
os.chdir(dir1)
dir1 = os.getcwd()

with open("stocks.csv", "r",
          encoding="utf-8") as input_file, open("output.csv", "w", encoding="utf-8") as output_file:

    output_file.write("Company Name,PE Ratio, PB Ratio\n")

    next(input_file)  # skip first line
    for line in input_file:
        row_wise_values = line.split(",")
        stock_name = row_wise_values[0]
        stock_price = float(row_wise_values[1])
        stock_eps = float(row_wise_values[2])
        stock_book_value = float(row_wise_values[3])
        pe_ratio = round(stock_price / stock_eps, 4)
        pb_ratio = round(stock_price / stock_book_value, 4)
        output_file.write(f"{stock_name},{pe_ratio},{pb_ratio}\n")
