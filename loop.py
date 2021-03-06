import time
import datetime
#import random
import RPi.GPIO as GPIO

def GPIOsetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.IN)

def mail_sensor():
    """ ...  """
    #return random.choice([0,1])
    return GPIO.input(16)



def cars_sensor():
    """ ... """
    #return random.choice([0,1,2])
    return GPIO.input(18)


def mail_status(detection):
    """Write the status text for the mailbox."""
    if detection == 0:
        return"Full!"
    elif detection == 1:
        return "Empty"
 

def cars_status(detection):
    """Write the status text for the carpark."""
    if detection == 0:
        return "InUse"
    elif detection == 1:
        return "Open!"


def read_sensor(location):
    """Choose which sensor to reference and return the detection."""
    if location == "mail":
        return mail_sensor()
    elif location == "cars":
        return cars_sensor()
    else:
        return f"no sensor installed for location '{location}'"


def write_status(location, detection):
    """Choose which status writer to employ."""
    if location == "mail":
        return mail_status(detection)
    elif location == "cars":
        return cars_status(detection)
    else:
        return f"-ERR- location '{location}'"


def determine(location):
    """Return the named status of location based off sensor's detection."""
    detection = read_sensor(location)
    return write_status(location, detection)


def log(time_stamp, mail_stat, cars_stat):
    """Write timestamp and location statuses to a log file."""
    with open('log.txt','a') as log:
        log.write('\n' + time_stamp + " | MAIL: " + mail_stat + " | CARS: " + cars_stat)


def store(location, status, time_stamp):
    """Writes status and timestamp to a "current" file
    for an outside program to reference."""
    with open(f'{location}_cur.txt','w') as current_file:
        current_file.write(status + '\n' + time_stamp)


def main():
    time_stamp = datetime.datetime.now().strftime("%Y-%b-%d | %H:%M:%S")
    mail_stat = determine("mail")
    cars_stat = determine("cars")
    log(time_stamp,mail_stat,cars_stat)
    store("mail",mail_stat,time_stamp)
    store("cars",cars_stat,time_stamp)


i = int(input("How long should I wait between checking the sensors? Secs: "))
GPIOsetup()
while True:
    main()
    time.sleep(i)
    
    
