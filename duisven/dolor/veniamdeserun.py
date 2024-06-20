     import pyautogui

     # Get the screen size
     screen_width, screen_height = pyautogui.size()

     # Move the window to the upper position
     window_width, window_height = pyautogui.size()
     pyautogui.moveTo(0, 0)
     