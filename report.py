# report.py
import csv
from datetime import datetime
import random

today = datetime.now().strftime("%Y-%m-%d")
total_sales = random.randint(1000, 5000)

filename = f'report_{today}.csv'

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Total Sales'])
    writer.writerow([today, total_sales])

print(f"Report generated: {filename} → Total Sales = {total_sales}")
