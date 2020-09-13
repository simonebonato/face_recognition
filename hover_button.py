from tkinter import *

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +85 #27 original
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter_box(event):
        toolTip.showtip(text)
        widget['bg'] = 'orange'
        widget['fg'] = 'black'
    def leave_box(event):
        toolTip.hidetip()
        widget['bg'] = 'blue'
        widget['fg'] = 'white'
    widget.bind('<Enter>', enter_box)
    widget.bind('<Leave>', leave_box)
    


# def enter(event,button):
#     button['bg'] = 'green'
# def leave(event,button):
#     button['bg'] = 'blue'