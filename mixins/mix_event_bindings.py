def mix_event_bindings(self, root):
    # (optional: keyboard + ) LBM
    root.bind("<Button-1>", self.left_click)
    # click and hold
    root.bind("<B1-Motion>", self.on_drag)
    # left mouse button release
    root.bind("<ButtonRelease-1>", self.on_release)
    # hover
    root.bind("<Motion>", self.on_enter)
    root.bind("<KeyPress-Control_L>", self.cursor.ctrl_ready)  # KeyPress
    root.bind('<KeyRelease-Control_L>', self.on_release)

