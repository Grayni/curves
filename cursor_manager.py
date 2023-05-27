class CursorManager:
    def __init__(self, widget):
        self.widget = widget
        self.arrow_path = "@assets/cursors/arrow.cur"
        self.arrow_minus_path = "@assets/cursors/arrow_minus.cur"
        self.hand_path = "@assets/cursors/hand.cur"
        self.drag_path = "@assets/cursors/drag.cur"
        self.default_cursor = self.widget.cget("cursor")
        self.previous_cursor = self.default_cursor

    def arrow_cursor(self):
        self.previous_cursor = self.widget.cget("cursor")
        self.widget.configure(cursor=self.arrow_path)

    def hand_cursor(self):
        self.previous_cursor = self.widget.cget("cursor")
        self.widget.configure(cursor=self.hand_path)

    def drag_cursor(self):
        self.widget.configure(cursor=self.drag_path)

    def cross_cursor(self):
        self.widget.configure(cursor="crosshair")

    def delete_cursor(self):
        self.widget.configure(cursor=self.arrow_minus_path)

    # def restore_cursor(self, event):
    #     self.widget.configure(cursor=self.previous_cursor)

    def ctrl_ready(self, event):
        if self.widget.allow_influence_point(event):
            self.delete_cursor()







