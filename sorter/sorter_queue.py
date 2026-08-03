from collections import deque


class SortQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, color):

        self.queue.append(color)

        print(f"ADD -> {color}")

    def pop(self):

        if len(self.queue) == 0:
            return None

        color = self.queue.popleft()

        print(f"EJECT -> {color}")

        return color

    def show(self):

        print(list(self.queue))