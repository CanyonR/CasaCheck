       __
    __/  \__
___/        \___
 |------------|
 | CASA CHECK |
 |------------|
 |   v. 0.1   |
 | 2020-02-13 |
----------------
----------------

1. Table of Contents
    1. Table of Contents
    2. About the Program
    3. List of Files
    4. Requirements
    5. Instructions
    6. About the Author


2. About the Program
    The end-goal is to use infrared (IR) sensors to check a house's
mailbox and carpark at a desired interval and concurrently allow a
website to display the most recent results. This version currently uses
simple random number functions as placeholders for physical sensors.

    When the mailbox and carpark sensors are checked, the timestamp
and status of each location is logged and saved to separate .txt files.
The {location}_cur.txt files can then be refereced while the main
process continues to run.


3. List of Files:
    + README.txt
    + log.txt
    + mail_cur.txt
    + cars_cur.txt
    + mod.py
    + loop.py
    + check.py
    + casa.py


4. Requirements:
    + Python 3 (developed in 3.7.4)
        - datetime
        - random
        - time
    + All files must be in the same folder


5. Instructions:
    + Run 'loop.py' to start the sensing/logging/saving process
        - When prompted, enter the desired interval (in seconds)
    + Run 'casa.py' to display the most recent statuses and timestamps


6. About the Author
    Canyon Read
        4+ Years in customer-facing tech industry roles
        B.A. Strategic Communication - Washington Sate University
        Brazilian Jiu-Jitsu White Belt
        San Jose, California, United States of America
