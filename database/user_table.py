class UserTable:
    def __init__(self, id=None, pwd=None, name=None, message=None, description=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.message = message
        self.description = description

    def __str__(self):
        return 'id: '+self.id+'pwd: '+self.pwd+'name: '+self.name+'message: '+self.message+'description: '+self.description