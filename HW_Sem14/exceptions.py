class AccessException(Exception):
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return f'ID {self.id} incorrect!'
    

class LevelException(Exception):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return f'Admin level cannot add users with level {self.level}!'