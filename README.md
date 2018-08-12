# Android Headset Media Controls for Windows
Python script that hacks in support for Android headset media control for Windows.

For more details on how this works, see the associated [blog post](http://www.roligheten.no/blog/programming/2018/07/02/media-controls-windows.html)

## Installation
Regardless of the platform the following is required
1. Python 3 or 2.7 (untested) installed on the system.
2. The packages pywin32 and sounddevice, installable via `pip install pywin32 sounddevice`.

### Windows
1. Download a copy of this repository from [here](https://github.com/Catuna/AndroidMediaControlsWindows/archive/master.zip)
2. Extract to an appropriate location on your system, where doesn't matter as long as you don't accidentally delete it.
3. Navigate to the following directory:

    `C:\Users\<your username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
4. Create a shortcut via File->New->Shortcut in the directory.

   When asked to specify location point it to where 'pythonw.exe' is installed.
   
   This is usually at:
   `C:\Users\<your username>\AppData\Local\Programs\Python\Python<version>\pythonw.exe`
   
   When prompted for shortcut name just keep the default.
5. Right-click the new shortcut and open 'properties'
6. At the end of 'target' add the path where you installed the 'run.py' script to the end of the string.
   
   For example:
   
   Target: `<path to pythonw.exe> C:\Programs\audiocontrols\run.py`
   
7. Restart your computer. At this point you should find 'pythonw.exe' running in the task mananger under 'Background Processes' and the program should function.

### Linux and Mac
Sorry, the script currently only works for Windows at the moment, feel free to contribute code for other platforms if you have the time.
