### LOAD LIBRARIES ###

# Data wrangling & processing: 
import numpy as np
import pandas as pd
from lxml import html
import requests
import json



### FETCH HISTORICAL DATA ###

## FUNCTION
# Define a function to fetch the historical data:
def fetchHistoricalPrices(u_a, extensions):
    
    # Name an empty dictionary to hold the data:
    nested_dict = {}
    
    # Scrape both websites:
    for product, ext in extensions.items():

        # Specify the url:
        url = 'https://www.investing.com' + ext

        # Access the website to request content:
        site = requests.get(url=url, headers=u_a)

        # Parse the HTML content:
        elem = html.fromstring(site.content)

        # Specify the XPath for the date element:
        dates = elem.xpath('//*[@id="curr_table"]/tbody/tr/td[1]/text()')

        # Specify the XPath for the price element:
        prices = elem.xpath('//*[@id="curr_table"]/tbody/tr/td[2]/text()')

        # Specify the product:
        nested_dict[product] = {}
        
        # Add the dates & prices as key-value pairs:
        nested_dict[product] = dict(zip(dates, prices))
    
    # The function returns the nested dictionary:
    return(nested_dict)




## PARAMETERS
# Declare a User-Agent to prevent "<Response [403]>" error & access the data:
u_a = {"User-Agent": "This is a web-scraping program. For questions, please contact heathersteich@gmail.com."}

# Create a dictionary with the product & extension for each website:
extensions = {'gold': '/commodities/gold-historical-data', 
              'silver': '/commodities/silver-historical-data'}




## EXECUTE FUNCTION
# Run the function, with parameters specified:
data = fetchHistoricalPrices(u_a, extensions)




## EXPORT DATA TO FILE
# Create an empty *.JSON file with 'write' priviledges:
with open("historical.json", "w") as file:
    
    # Dump the nested dictionary to the file:
    json.dump(data, file)
    
    # Update the user:
    print('Created file: ', file.name, 
          '\n. . .'
          '\nExecution complete.')