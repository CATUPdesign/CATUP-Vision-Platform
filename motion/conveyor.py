class Conveyor:

    def __init__(self):

        self.position = 0

    def update(self):

        self.position += 1

    def get_position(self):

        return self.position