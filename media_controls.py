import win32api
import win32con

VK_MEDIA_PLAY_PAUSE = 0xB3

def toggle_play():
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
