import PyPDF2
import statistics
import csv
from datetime import datetime, timedelta

try:
    file=input()
    result=0

    if file!="":        
        row = []
        pdf_file=PyPDF2.PdfReader(open(file,"rb"))
        number_of_pages=len(pdf_file.pages)
        page1=pdf_file.pages[0]
        page2=pdf_file.pages[1]
        text1=page1.extract_text()
        text2=page2.extract_text()

        pos1=text1.find("Apmaksai")
        pos2=text1.find("Elektroenerģijas patēriņš")
        pos3=text1.find("Veicot")
    
        text1=text1.replace(',','.')
        text2=text2.replace(',','.')

        total_charge = float(text1[pos1+10:pos2].strip())
        quantity = float(text1[pos2+31:pos3].strip().replace(' ', '').replace('kWh', ''))

        pos4 = text2.find("Apjoms")
        time_frame = text2[pos4-23:pos4].strip()

        start_day = time_frame[0:2]
        start_month = time_frame[3:5]
        start_year = time_frame[6:10]
        end_day = time_frame[13:15]
        end_month = time_frame[16:18]
        end_year = time_frame[19:23]

        time_start = start_year+"-"+start_month+"-"+start_day
        time_end = end_year+"-"+end_month+"-"+end_day
        date_format = "%Y-%m-%d"
        end_date = (datetime.strptime(time_end, date_format) + timedelta(days=1)).strftime(date_format)

        pos5 = text2.find('kWh')
        price_per_kwh = float(text2[pos5+3:pos5+10].strip())

        nordpool_values = []
        nordpool_avg=0

        with open("nordpool.csv", "r") as f:
            nordpool_data = csv.reader(f)
            next(nordpool_data)

            for row in nordpool_data:
                start_time, end_time, value = row
                if time_start <= start_time <= end_date:
                    nordpool_values.append(float(value))

    nordpool_avg = statistics.mean(nordpool_values)

    if quantity==0:
        result=0
    else:
        nordpool_total = quantity * round(nordpool_avg, 3)
        current_total = quantity * price_per_kwh
        savings = current_total - nordpool_total
        result = round(savings, 1)

    print(result)
except:
    print(0)
