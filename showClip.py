#!/usr/bin/python3
from gi.repository import Gtk, Gdk

EMPTY = 'N/A'

def create_clipboard(callback):
    clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    clip.connect('owner-change', callback) 
    return clip

def create_clear_button(callback):
    button = Gtk.Button(label='Clear')
    button.connect('clicked', callback)
    return button

class ShowClipWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Show Clipboard')
        self.setup_window()
        self.clip = create_clipboard(self.update_view)
        self.label = Gtk.Label(EMPTY)
        self.layout_window(create_clear_button(self.clear_clipboard), self.label) 

    def setup_window(self):
        self.set_icon_name(Gtk.STOCK_PASTE)
        self.set_keep_above(True)
        self.set_default_size(240, 200)

    def layout_window(self, button, label):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        box.pack_start(button, False, False, 3)
        box.pack_start(label, True, True, 0)
        self.add(box)

    def update_view(self, clipboard, event):
        clip_text = clipboard.wait_for_text()
        if clip_text:
            self.label.set_text(clip_text)

    def clear_clipboard(self, source):
        self.clip.set_text('', -1)
        self.label.set_text(EMPTY)

win = ShowClipWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
