import requests, os
from requests.auth import HTTPBasicAuth
from model.drink import Drink
from dotenv import load_dotenv
from view.util import alert_message

load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def drinks():
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/drinks"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            data = []
            for row in raw:
                data.append(
                    Drink(int(row["id"]), row["name"], int(row["price"]), int(row["category"]))
                )
            return data
        else:
            return
    except Exception as e:
        alert_message(e)


async def get_drink(id=None):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/drink"
        response = requests.get(url, headers=headers, auth=auth, params={"id": id})
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            if not raw:
                return None
            else:
                raw = raw[0]
                return Drink(int(raw["id"]), raw["name"], int(raw["price"]), int(raw["category"]))
        else:
            return None
    except Exception as e:
        alert_message(e)


async def delete_drink(id=None):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/drink"
        response = requests.delete(url, headers=headers, auth=auth, params={"id": id})
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)


async def change_drink(drink):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/drink"
        response = requests.put(
            url,
            headers=headers,
            auth=auth,
            json={
                "id": drink.id,
                "category": drink.category,
                "name": drink.name,
                "price": drink.price,
            },
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)


async def add_drink(drink):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/drink"
        response = requests.post(
            url,
            headers=headers,
            auth=auth,
            json={"category": drink.category, "name": drink.name, "price": drink.price},
        )
        if response.status_code == 200:
            raw = response.json()["data"]["rows"][0]["id"]
            drink.id = int(raw)
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)
