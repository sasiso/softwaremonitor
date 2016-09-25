
# software monitor
---------------------------------------------------------------------------
Displays statics of software on time scale. Example resource usages, Error, Warnings
A source with multiple channels can be added
For example, Logging from different processes

Current target is to add logging as input channel.
Display will render all events happening in process on time scale
For Example - User Actions, Success Failures, Crashes, Warnings
            - Ideally events are just regular expression and assigned ( user can configure which UI element to display)
            - See mock-up folder.


Possible User Interactions
---------------------------------------------------------------------------
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
- Allow user to pause

See Current Work
---------------------------------------------------------------------------
Run Line.py
Run main.py

Engine Work
----------------------------------------------------------------------------

Next Development Task
Implement simple logging parser
  To read time and information and render them on display engine

Implement source manager to handle different sources
  Display engine will query source manager to give channel data for each source
  Display engine will show line for each channel in source


UI Work
---------------------------------------------------------------------------

Challenge
---------------------------------------------------------------------------
- How To keep Display engine response regardless of source performance
  For example a source who reads log file may take a long time
  display engine shall just time out not wait longer





Developer Setup
---------------------------------------------------------------------------
- Install Python from Welcome to Python.org
- Install PyCharm Community Edition frnom www.jetbrains.com/PyCharm
- Once Python is installed
    Install PySide ( for QT)
    Install PyOpenGl ( for OpenGL)
- Now open PyCharm, Create a project with Root Directory of Source code
- Configure Python interpreter, You are ready to go....





Good to have
---------------------------------------------------------------------------
- Identify known patterns from input template



Technically
---------------------------------------------------------------------------
- Is it good to have own database
   - will keep small runtime memory footprint
   - Will help in exporting , Saving ( session, MP4)
