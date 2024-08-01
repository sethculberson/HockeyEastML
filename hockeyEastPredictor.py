import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

def getStandings():
    years = ['2122','2223','2324']
    for year in years:
        url = f"https://www.hockeyeastonline.com/men/statistics/{year}/conference-team.php"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        data = []

        table = soup.find('table')
        table_headers = table.find_all('th')
        table_rows = table.find('tbody').findAll('tr')

        header_data = []
        for header in table_headers:
            header_data.append(header.text)
        data.append(header_data)


        for row in table_rows:
            row_data = []
            for cell in row.find_all('td'):
                row_data.append(cell.text)
            data.append(row_data)

        df = pd.DataFrame(data)

        path = 'data/standings'
        df.to_csv(f"{path}/Hockey-East-Standings-{year}.csv",index=False)

def getTeamStats(team):
    url = f"https://www.hockeyeastonline.com/men/{team}/2023-24-statistics.php"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    
    table = soup.find('table')
    
    table_headers = table.find_all('th')
    table_rows = table.find('tbody').findAll('tr')

    header_data = []
    for header in table_headers:
        header_data.append(header.text)
    data.append(header_data)


    for row in table_rows:
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        data.append(row_data)

    df = pd.DataFrame(data)
    
    df = pd.DataFrame(data)
    path = 'data/teamStats'
    df.to_csv(f"{path}/{team}-stats.csv",index=False)
    
schools = ['boston-college','boston-university','uconn','maine','massachusetts','umass-lowell','merrimack','new-hampshire','northeastern','providence','vermont']
for school in schools:
    getTeamStats(school)