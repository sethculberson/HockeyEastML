import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.hockeyeastonline.com/men/statistics/2324/conference-team.php"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data = []

table = soup.find('table')
table_rows = table.find_all('tr')

for row in table_rows:
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    data.append(row_data)

df = pd.DataFrame(data)

time.sleep(1)

print(df)
#df.to_csv('Hockey-East-Standings.csv',index=False)