import requests, os
from requests.auth import HTTPBasicAuth
from model.employee import Employee
from dotenv import load_dotenv
from view.util import alert_message

load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def employees():
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/employees"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            data = []
            for row in raw:
                data.append(
                    Employee(
                        int(row["id"]),
                        int(row["position"]),
                        int(row["gender"]),
                        row["name"],
                        row["username"],
                        row["psw"],
                        row["active"],
                        row["created_at"],
                    )
                )
            return data
        else:
            return []
    except Exception as e:
        alert_message(e)


async def get_employee(id=None):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/employee"
        response = requests.get(url, headers=headers, auth=auth, params={"id": id})
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            if not raw:
                return None
            else:
                raw = raw[0]
                return Employee(
                    int(raw["id"]),
                    int(raw["position"]),
                    int(raw["gender"]),
                    raw["name"],
                    raw["username"],
                    raw["psw"],
                    raw["active"],
                    raw["created_at"],
                )
        else:
            return None
    except Exception as e:
        alert_message(e)


async def delete_employee(id=None):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/employee"
        response = requests.delete(url, headers=headers, auth=auth, params={"id": id})
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)


async def change_employee(employee):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/employee"
        response = requests.put(
            url,
            headers=headers,
            auth=auth,
            json={
                'id':employee.id,
                'position':employee.position,
                'gender':employee.gender,
                'name':employee.name,
                'username':employee.username,
                'psw':employee.psw,
                'active':employee.active
            },
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)


async def add_employee(employee):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/employee"
        response = requests.post(
            url,
            headers=headers,
            auth=auth,
            json={
                'position':employee.position,
                'gender':employee.gender,
                'name':employee.name,
                'username':employee.username,
                'psw':employee.psw,
            },
        )
        if response.status_code == 200:
            raw = response.json()["data"]["rows"][0]
            employee.id = int(raw["id"])
            employee.created_at = raw["created_at"]
            return True
        else:
            return False
    except Exception as e:
        alert_message(e)
