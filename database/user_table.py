class UserTable:
    def __init__(self, id=None, pwd=None, name=None, email=None, message=None, description=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email
        self.message = message
        self.description = description

    def __str__(self):
        return 'id:'+self.id