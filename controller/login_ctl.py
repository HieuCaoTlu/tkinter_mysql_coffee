import requests, os
from requests.auth import HTTPBasicAuth
from model.employee import Employee
from dotenv import load_dotenv
from view.util import alert_message
load_dotenv()

async def login(user,psw):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/login"
        headers = {"accept": "application/json"}
        auth = HTTPBasicAuth(os.getenv('ADM'),os.getenv('APASS'))
        response = requests.get(url, headers=headers, auth=auth, params={'username':user,'psw':psw})
        if response.status_code == 200:
            raw = response.json()['data']['rows']
            if not raw:
                return
            else:
                raw = raw[0]
                return Employee(int(raw['id']),int(raw['position']),int(raw['gender']),raw['name'],raw['username'],raw['psw'],raw['created_at'])
        else:
            return
    except Exception as e:
        alert_message(e)