class CursorManager:
    def __init__(self):
        self.hand_path = "@assets/cursors/hand.cur"
        self.drag_path = "@assets/cursors/drag.cur"

    def hand_cursor(self, event):
        event.widget.configure(cursor=self.hand_path)

    def drag_cursor(self, event):
        event.widget.configure(cursor=self.drag_path)

    @staticmethod
    def arrow_cursor(event):
        event.widget.configure(cursor="arrow")

    def cross_cursor(self, event):
        self.configure(cursor="crosshair")

    def delete_cursor(self):
        self.configure(cursor="circle")

    def ctrl_ready(self, event):
        if event.keysym == 'Control_L' or event.keysym == 'Control_R':
            self.delete_cursor()




