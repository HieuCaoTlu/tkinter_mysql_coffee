import requests, os
from requests.auth import HTTPBasicAuth
from model.invoice import Invoice, InvoiceDrink
from dotenv import load_dotenv
from view.util import alert_message
load_dotenv()

headers = {"accept": "application/json"}
auth = HTTPBasicAuth(os.getenv("ADM"), os.getenv("APASS"))


async def invoices():
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/invoices"
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            data = []
            for row in raw:
                data.append(
                    Invoice(
                        int(row["id"]),
                        float(row["amount"]),
                        float(row["tax"]),
                        float(row["discount"]),
                        float(row["total"]),
                        int(row["employee"]),
                        row["employee_name"],
                        row["created_at"],
                    )
                )
            return data
        else:
            return
    except Exception as e:
        alert_message(e)


async def get_invoice_drink(id=None):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/invoice_drink"
        response = requests.get(url, headers=headers, auth=auth, params={"id": id})
        if response.status_code == 200:
            raw = response.json()["data"]["rows"]
            if not raw:
                return []
            else:
                data = []
                for row in raw:
                    ivc = InvoiceDrink()
                    ivc.invoice = int(row["invoice"])
                    ivc.drink = int(row["drink"])
                    ivc.quantity = int(row["quantity"])
                    ivc.drink_name = row["drink_name"]
                    ivc.price = row["price"]
                    data.append(ivc)
                return data
        else:
            return []
    except Exception as e:
        alert_message(e)


async def add_invoice(invoice, list):
    try:
        url = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/invoice"
        response = requests.post(
            url,
            headers=headers,
            auth=auth,
            json={
                "amount": invoice.amount,
                "tax": invoice.tax,
                "discount": invoice.discount,
                "total": invoice.total,
                "employee": invoice.employee.id,
            },
        )
        if response.status_code == 200:
            raw = response.json()["data"]["rows"][0]
            invoice.id = int(raw["id"])
            invoice.created_at = raw["created_at"]
            url2 = "https://ap-southeast-1.data.tidbcloud.com/api/v1beta/app/dataapp-OiUZnSiQ/endpoint/invoice_drink"
            count = 0
            for each in list:
                rsp = requests.post(
                    url2,
                    headers=headers,
                    auth=auth,
                    json={
                        "drink": each.drink.id,
                        "invoice": invoice.id,
                        "quantity": each.quantity,
                        "drink_name": each.drink_name,
                        "price": each.price,
                    },
                )
                if rsp.status_code == 200:
                    count += 1
            if count == len(list):
                return True
            return False
        else:
            return False
    except Exception as e:
        alert_message(e)
