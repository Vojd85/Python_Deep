class User:
    def __init__(self, user_id, name, level=7):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'{self.user_id} {self.name} {self.level}'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name