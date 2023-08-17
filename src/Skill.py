class Skill:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f'Skill: {self.name} ({self.id})'

    def __repr__(self):
        return self.__str__()