from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

my_columns = ['Time',
              'ITE',
              'Capacity',
              'Demand']

final_dataframe = pd.DataFrame(columns=my_columns)

while True:
    url = 'http://www.ercot.com/content/cdr/html/real_time_system_conditions.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    current_time = soup.findAll('div', attrs={'class': 'schedTime rightAlign'})
    currenttime = current_time[0].text.removeprefix('Last Updated: ')
    data = soup.findAll('td', attrs={'class': 'labelClassCenter'})
    ITE = data[1].text
    Capacity = data[3].text
    Demand = data[4].text
    final_dataframe = final_dataframe.append(
        pd.Series(
            [
                currenttime,
                ITE,
                Capacity,
                Demand,

            ],
            index=my_columns),
        ignore_index=True
    )
    final_dataframe.to_csv('Ercot.csv', mode='w', header=True)
    time.sleep(30)