import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

url = "https://www.skysports.com/premier-league-table"

# Pagination 
src = requests.get(url)
soup = BeautifulSoup(src.text, 'html.parser')
df = pd.read_html(url, index_col='#')
table = df[0].drop(columns='Last 6')