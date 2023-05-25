def mix_event_bindings(self):
    # (optional: keyboard + ) LBM
    self.bind("<Button-1>", self.left_click)
    # click and hold
    self.bind("<B1-Motion>", self.on_drag)
    # left mouse button release
    self.bind("<ButtonRelease-1>", self.on_release)
    # hover
    self.bind("<Motion>", self.on_enter)
    self.root.bind("<KeyPress-Control_L>", self.cursor.ctrl_ready)  # KeyPress
    self.root.bind('<KeyRelease-Control_L>', self.on_release)

