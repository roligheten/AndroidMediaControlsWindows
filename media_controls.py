import platform

OS = platform.system()

if OS == "Linux":
    import os
elif OS == "Windows":
    import win32api
    import win32con
    VK_MEDIA_PLAY_PAUSE = 0xB3


def toggle_play():
    if OS == "Linux":
        os.system('xdotool key XF86AudioPlay')
    elif OS == "Windows":
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
