import datetime, calendar
import pandas as pd
from dateutil.relativedelta import relativedelta #https://dateutil.readthedocs.io/en/stable/relativedelta.html
import requests
import json, os
from dotenv import load_dotenv

load_dotenv()

def get_months_to_date():
    today = datetime.date.today() - datetime.timedelta(days=1)
    last_two_months_to_date = today - relativedelta(months=5) 
   
    days = []
    while last_two_months_to_date <= today: # fetch each days for the last two months
        days.append(last_two_months_to_date)
        last_two_months_to_date += datetime.timedelta(days=1)
    

    weeks = []
    for seven_days in range(0, len(days), 7):
        week = days[seven_days:seven_days + 7]
        
        weeks.append({
            "start_date": week[0],
            "end_date": week[-1]
        })  
  
    df = pd.DataFrame(weeks)

    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['start_date'] = df['start_date'].dt.strftime('%d%m%Y')
    df['end_date']   = df['end_date'].dt.strftime('%d%m%Y')
    
    return df


if __name__ == '__main__':
    df = get_months_to_date()

    for idx, row in df.iterrows():
        start = row['start_date']
        end = row['end_date']
        print(start, end)

    
    
    

# def get_days_in_month(year, month):
#     day = calendar.monthcalendar(year, month)
#     days = [day for week in week for day in week if day != 0] 

#     weeks = []
#     for seven_days in range(0, len(days), 7):
#         week = days[seven_days:seven_days + 7]
#         first_day = week[0]
#         last_day = week[-1]
#         weeks.append((f"{first_day}", f"{last_day}"))
#     print(weeks)
#     return days