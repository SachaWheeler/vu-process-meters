import pygetwindow as gw
x = gw.getAllTitles()
print(x)
"""
import wnck
window_list = wnck.screen_get_default().get_windows()
print(window_list)

import Xlib.display
display = Xlib.display.Display()
print(display)
window = display.get_input_focus().focus
print(window)
wmname = window.get_wm_name()
wmclass = window.get_wm_class()
if wmclass is None and wmname is None:
    window = window.query_tree().parent
    wmname = window.get_wm_name()
print("WM Name: %s" % ( wmname, ))

"""
