import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

# URL of the Premier League table page on Sky Sports website
url = "https://www.skysports.com/premier-league-table"

# Send GET request to the URL and retrieve the source code
src = requests.get(url)

# Parse the HTML of the page using BeautifulSoup
soup = BeautifulSoup(src.text, 'html.parser')

# Use pandas to read the HTML table on the page and create a DataFrame
df = pd.read_html(url, index_col='#')

# Drop the 'Last 6' column from the DataFrame
table = df[0].drop(columns='Last 6')
print(table)
