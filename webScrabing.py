import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = 'https://www.example.com'

# Fetch the HTML content of the URL
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the data to scrape
data = []
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    row_data = []
    for column in columns:
        row_data.append(column.text.strip())
    if row_data:
        data.append(row_data)

# Save the data to a CSV file
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)



