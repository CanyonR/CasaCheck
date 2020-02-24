          __
       __/  \__
  ____/________\____
   |--------------|
   |  CASA CHECK  |
   |--------------|
   |   v 0.2.0    |
   |  2020-02-23  |
----------------------
----------------------

1. Table of Contents
    1. Table of Contents
    2. About the Program
    3. List of Files
    4. Requirements
    5. Instructions
    6. About the Author
    7. To-Do List


2. About the Program
    Uses infrared (IR) sensors to check a house's mailbox and carpark
at a desired interval.
    When the mailbox and carpark sensors are checked, the timestamp
and status of each location is logged and saved to separate .txt files.
The most recent results can then be refereced while the main
process continues to run.


3. List of Files:
    + README.txt
    + log.txt
    + mail_cur.txt
    + cars_cur.txt
    + loop.py
    + check.py
    + casa.py


4. Requirements:
    + Raspberry Pi
    + Python 3 (developed in 3.7.4)
        Modules:
        - datetime
        - time
        - RPi.GPIO


5. Instructions:
    + If you want to move the log and {location}_cur files,
        the file-paths can be adjusted in loop.log() and loop.store().
    + The GPIO pin numbers can be adjusted in loop.GPIOsetup().
    + Run 'loop.py' to start the sensing/logging/saving process.
        - When prompted, enter the desired interval (in seconds).
    + Run 'casa.py' to display the most recent statuses and timestamps.


6. About the Author
    Canyon Read
        CompTIA Network+ Certified
        B.A. Strategic Communication - Washington Sate University
        San Jose, California, United States of America


7. To-Do List
    o Print error messages to the terminal
