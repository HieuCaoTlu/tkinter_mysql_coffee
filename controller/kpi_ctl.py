import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from view.util import alert_message
from model.kpi import KPI

load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def get_kpi():
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/kpi"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            if not raw:
                return None
            else:
                raw = raw[0]
                return KPI(
                    int(raw["year"]),
                    int(raw["month"]),
                    int(raw["value"]),
                    int(raw["edit"]),
                )
        else:
            return None
    except Exception as e:
        alert_message(e)


async def change_kpi(kpi):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/kpi"
        response = requests.put(
            url,
            headers=headers,
            auth=auth,
            json={
                "value": kpi.value,
            },
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)


async def add_kpi(kpi):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/kpi"
        response = requests.post(
            url,
            headers=headers,
            auth=auth,
            json={"value": kpi.value},
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)
