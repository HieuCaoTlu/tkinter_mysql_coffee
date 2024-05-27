from requests.auth import HTTPBasicAuth
from model.category import Category
from dotenv import load_dotenv
import requests, os
from view.util import alert_message

load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def categories():
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/categories"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            data = []
            for row in raw:
                data.append(
                    Category(int(row['id']),row['name'])
                )
            return data
        else:
            return
    except Exception as e:
        alert_message(e)
