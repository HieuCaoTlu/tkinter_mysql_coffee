class Invoice:
    def __init__(self, id=0, amount=0,tax=0,discount=0,total=0,employee=None,employee_name=None,created_at=None):
        self.id = id
        self.amount = amount
        self.tax = tax
        self.discount = discount
        self.total = total
        self.employee = employee
        self.employee_name = employee_name
        self.created_at = created_at

class InvoiceDrink:
    def __init__(self):
        self.invoice = None
        self.drink = None
        self.quantity = 0
        self.drink_name = ''
        self.price = 0

