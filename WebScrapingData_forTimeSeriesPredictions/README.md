# Web Scraping Data for Time Series Predictions  
## Silver & Gold Prices  
---  
  
## A Combined Notebook of Three Individual, Executable `*.py` Programs  
  
**By: Heather M. Steich, M.S.**  
**Date: February 24$^{th}$, 2018**  
**Written in: Python 3.4.5**  
  
---  
  
# Project Contents  
  
> 1. Write a program to fetch the historical prices and dates of gold and silver from these 2 URLs:  
  
>  - [https://www.investing.com/commodities/gold-historical-data](https://www.investing.com/commodities/gold-historical-data)  
  
>  - https://www.investing.com/commodities/silver-historical-data  
  
>  and store them locally.  
  
> (Extract the default data range in each case: no need to interact with the UI elements.)  
  
> 2. Write a second program that takes the following 3 command line arguments:  
  
>  - Start date (in the format 2017-05-10)

>  - End date (in the format 2017-05-22)

>  - Commodity type (either "gold" or silver”)

>  and then returns (via the locally stored data) the mean and variance of the commodity’s price over the specified date range.  
  
> For example, the program might be called like so:  
  
> `In []:   ./getCommodityPrice 2017-05-01 2017-05-03 gold`  
  
> and would print out a tuple such as:  
  
> `Out []:   gold 1253.66 35.79`  
  
> 3. Lastly, write a program to help decide if the previous gold or silver prices are good predictors for their future prices.  
  
>  Also do the same to check if an increase or decrease in the price is predictable. (There is no need to do the actual prediction.)  