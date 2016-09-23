Developer Setup
- Install Python from Welcome to Python.org
- Install PyCharm Community Edition from www.jetbrains.com/PyCharm
- Once Python is installed
    Install PySide ( for QT)
    Install PyOpenGl ( for OpenGL)
- Now open PyCharm, Create a project with Root Directory of Source code
- Configure Python interpreter, You are ready to go....

# software monitor
Displays statics of software on time scale.
Different channels can be added into display.

Current target is to add logging as input channel.
Display will render all events happening in process on time scale
For Example - User Actions, Success Failures, Crashes, Warnings
            - Ideally events are just regular expression and assigned ( user can configure which UI element to display)
            - See mock-up folder.

Possible User Interactions
- Open the location for input (i.e. logs folder)
- Zoom in/out to increase or decrease time precision
- Enable Disable Grid on display
- Add new expressions (i.e. key word to search and mark)
- Mouse Hover tooltip
- Save total statistics ( pdf, png)
- Save / capture as PNG or export whole playback as MP4
- Scroll to move left and right on time scale
- Annotate findings
- Configure alarm for specific occurrence
- Allow user to open file on click ( if source is log file)



Good to have
- Identify known patterns from input template



Technically
- Is it good to have own database
   - will keep small runtime memory footprint
   - Will help in exporting , Saving ( session, MP4)
