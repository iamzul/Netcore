from src.utils.date import get_months_to_date
from dotenv import load_dotenv
import pandas as pd
import os, requests


load_dotenv()

def get_activity(start, end, email):
    # activity id for article_page_load is 103
    url = f"https://api.netcoresmartech.com/apiv2?type=export_data&activity=get_user_activity_data&apikey={os.getenv('netcore_apikey')}"
    payload = f'data={{"primary_key":"{email}","from_date":"{start}","to_date":"{end}","activity_id": 103}}'
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    # print(response)
    result = response.get('result', [])
    activities_data = result.get('activity_data',[])
    if not activities_data:
        return
    activities = []
    for activity in activities_data:
        activities.append({
            'netcore_id' : activity.get('uid'),
            'email': email,
            'activity_id' : activity.get('ev'),
            'page_url' : activity.get('page_url'),
            'title': activity.get('title'),
            'category' : activity.get('category'),
            'segment' : activity.get('segment'),
            'event_type' : activity.get('event_type'),
            'activity_datetime' : activity.get('activity_date_time')    
        })
    
    return activities



def main():
    activities = []
    emails = ["zulkifliarshd@gmail.com","norhayatiabubakar3@gmail.com"]
    date = get_months_to_date()
    for email in emails:
        for idx, row in date.iterrows():
            start = row['start_date']
            end = row['end_date']
            result = get_activity(start, end, email)
            if result:
                activities.extend(result)
    
    activities = pd.DataFrame(activities)
    activities.to_csv('user_logins.csv', index=False)
    print(activities)
        
        
    

if __name__ == '__main__':
    main()