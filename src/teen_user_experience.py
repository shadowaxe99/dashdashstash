class TeenUserExperience:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, {self.name}! Welcome to the Teen User Experience.')


if __name__ == '__main__':
    user = TeenUserExperience('John')
    user.greet()