import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from view.util import alert_message

load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def get_other():
    try:
        url = f"{os.getenv('API')}/other"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            if not raw:
                return None
            else:
                raw = raw[0]
                return (int(raw['tax']),int(raw['discount']))
        else:
            return None
    except Exception as e:
        alert_message(e)


async def change_other(tax, discount):
    try:
        url = f"{os.getenv('API')}/other"
        response = requests.put(
            url,
            headers=headers,
            auth=auth,
            json={
                "tax": tax,
                "discount": discount
            },
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)