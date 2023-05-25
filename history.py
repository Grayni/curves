from collections import deque


class History:
    def __init__(self):
        self.history_steps = deque(maxlen=3)

    def save_step(self, state):
        self.history_steps.append(state)

    def load_step(self):
        step = self.history_steps[-1]

    def show_history(self):
        print(self.history_steps)




