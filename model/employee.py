class Employee:
    def __init__(self, id=None, position=None, gender=None, name=None, username=None, psw=None, active=None, created_at=None):
        self.id = id
        self.position = position
        self.gender = gender
        self.name = name
        self.username = username
        self.psw = psw
        self.active = active
        self.created_at = created_at

    def getGender(self):
        return 'Nam' if self.gender else 'Nữ'
    
    def getRole(self):
        return 'Quản trị' if self.role else 'Nhân viên'