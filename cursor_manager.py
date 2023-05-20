class CursorManager:
    def __init__(self):
        self.arrow_path = "@assets/cursors/arrow.cur"
        self.arrow_minus_path = "@assets/cursors/arrow_minus.cur"
        self.hand_path = "@assets/cursors/hand.cur"
        self.drag_path = "@assets/cursors/drag.cur"

    def allow_influence_point(self, event):
        pass

    def allow_add_point(self, event):
        pass

    def arrow_cursor(self):
        self.previous_cursor = self.cget("cursor")
        self.configure(cursor=self.arrow_path)

    def hand_cursor(self, event):
        self.previous_cursor = self.cget("cursor")
        self.configure(cursor=self.hand_path)

    def drag_cursor(self):
        self.configure.configure(cursor=self.drag_path)

    def cross_cursor(self):
        self.previous_cursor = self.cget("cursor")
        self.configure(cursor="crosshair")

    def delete_cursor(self):
        self.configure(cursor=self.arrow_minus_path)

    def restore_cursor(self, event):
        self.configure(cursor=self.previous_cursor)

    def ctrl_ready(self, event):
        if self.allow_influence_point(event):
            self.delete_cursor()







