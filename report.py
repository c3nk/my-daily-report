# report.py
import csv
from datetime import datetime
import random

today = datetime.now().strftime("%Y-%m-%d")
total_sales = random.randint(1000, 5000)

with open('report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Total Sales'])
    writer.writerow([today, total_sales])

print(f"Report generated for {today}: Total Sales = {total_sales}")
