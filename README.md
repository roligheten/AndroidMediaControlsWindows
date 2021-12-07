# Android Headset Media Controls for Windows and Linux
Python script that hacks in support for Android headset media control for Windows and Linux

For more details on how this works, see the associated [blog post](http://www.roligheten.no/blog/programming/2018/07/02/media-controls-windows.html)

## Installation

### Dependencies

#### On Windows
Regardless of the platform the following is required
1. Python 3 or 2.7 (untested) installed on the system.
2. The packages pywin32 and sounddevice, installable via `pip install pywin32 sounddevice`.
#### On Linux
##### Note: This only works on X11, No wayland Support as of now
1. Install python3 via `sudo apt install python3`
2. install packages sounddevice and numpy `pip3 install numpy sounddevice`
3. install xdotool (emulates key presses) `sudo apt install xdotool`
4. Install pypy, found to give performence improvements; recommended but not required, you can use the regular python interpreter: `sudo apt install pypy3`
if run via pypy, install requirements using `pypy3 -m pip install numpy sounddevice`

### Running and Installing

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

### Linux

1. Clone the repo via `git clone <url>` or download and extract the zip as listed in the first step of the windows install
2. Place it somewhere safe, maybe in the documents folder
3. cd into the directory
4. start the script via `python3 run.py` or `pypy3 run.py`, test if it works if you want to
5. test if it works
6. then add it to startup apps, as of Pop!_OS 21.04, you can do this via the startup apps application

### Mac
Not yet supported


