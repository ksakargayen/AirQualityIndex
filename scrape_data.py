import requests
from bs4 import BeautifulSoup
# import pandas as pd
import csv


def to_float(val):
	try:
		return float(val)
	except ValueError:
		return val


def clean_text(text_data):
	text = to_float(text_data)
	if isinstance(text, bytes):
		text = text.replace(b'\xc2\xa0', b'').replace(b'-', b'')

	return text


def write_to_csv(table_data, name):
	with open(f'Data/{name}.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(table_data)
	print("File written:\t", name)


def get_climate_index():
	for year in range(2013, 2019):
		for month in range(1, 13):
			date = f"0{month}-{year}" if month < 10 else f"{month}-{year}"
			
			URL = f"https://en.tutiempo.net/climate/{date}/ws-426670.html"

			page = requests.get(URL)

			soup = BeautifulSoup(page.content, 'html.parser')

			table = soup.find_all('table')[3]
			
			table_data = []
			for child in table.children:
				row_data = []
				for tr in child:
					text = clean_text(tr.text.encode('utf-8'))
					row_data.append(text)
				table_data.append(row_data)
			
			write_to_csv(table_data, date)

	return "Finished"


if __name__ == '__main__':
	r = get_climate_index()
	print("Rows:\t", r)

	# Assert len of headers as 15 and len of rows as 465