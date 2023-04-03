# import requests
# from bs4 import BeautifulSoup
# import json


# # Make a request to the URL with the table
# url = "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days"
# response = requests.get(url)

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the table element using its tag name
# table = soup.find("table")

# # Get the table headers
# headers = []
# for th in table.find_all("th"):
#     headers.append(th.text.strip())

# # Get the table rows
# rows = []
# for tr in table.find_all("tr")[1:]:
#     cells = {}
#     tds = tr.find_all("td")
#     date = tr.find("th").text.strip()
#     for i in range(len(tds)):
#         header = headers[i+1] if i+1 < len(headers) else 'Notes'
#         cells[header] = tds[i].text.strip()
#     cells['Date'] = date
#     rows.append(cells)

# print(json.dumps(rows))

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/table_data')
def get_table_data():
    # Make a request to the URL with the table
    url = "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days"
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element using its tag name
    table = soup.find("table")

    # Get the table headers
    headers = []
    for th in table.find_all("th"):
        headers.append(th.text.strip())

    # Get the table rows
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = {}
        tds = tr.find_all("td")
        date = tr.find("th").text.strip()
        for i in range(len(tds)):
            header = headers[i+1] if i+1 < len(headers) else 'Notes'
            cells[header] = tds[i].text.strip()
        cells['Date'] = date
        rows.append(cells)

    # Return the table data as JSON
    return jsonify(rows)

if __name__ == '__main__':
    app.run()
