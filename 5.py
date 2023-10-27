from bs4 import BeautifulSoup
import csv

with open("text_5_var_11") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table")

with open("result_text_5_var_11", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    headers = [header.text for header in table.find_all("th")]
    csvwriter.writerow(headers)
    rows = table.find_all("tr")
    for row in rows[1:]:
        cells = row.find_all("td")
        row_data = [cell.text for cell in cells]
        csvwriter.writerow(row_data)
