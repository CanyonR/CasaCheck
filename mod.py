import datetime
import random


def mail_sensor():
    """Randomly choose from a list
    (instead of checking the output from physical sensor, as is planned)."""
    detection = random.choice([0,1])
    return detection


def cars_sensor():
    """Randomly choose from a list
    (instead of checking the output from physical sensor, as is planned)."""
    detection = random.choice([0,1,2])
    return detection


def mail_status(detection):
    """Write the status text for the mailbox."""
    if detection == 0:
        status = "empty"
    elif detection == 1:
        status = "full!"
    else:
        status = "-ERR- sens '{}'".format(detection)
    return status


def cars_status(detection):
    """Write the status text for the carpark."""
    if detection == 0:
        status = "Empty"
    elif detection == 1:
        status = "InUse"
    elif detection == 2:
        status = "Full!"
    else:
        status = "-ERR- sens '{}'".format(detection)
    return status


def read_sensor(location):
    """Choose which sensor to reference and return the detection."""
    if location == "mail":
        detection = mail_sensor()
        return detection
    elif location == "cars":
        detection = cars_sensor()
        return detection
    else:
        return f"no sensor installed for location '{location}'"


def write_status(location, detection):
    """Choose which status writer to employ."""
    if location == "mail":
        status = mail_status(detection)
        return status
    elif location == "cars":
        status = cars_status(detection)
        return status
    else:
        return f"-ERR- location '{location}'"


def determine(location):
    """Return the named status of location based off sensor's detection."""
    detection = read_sensor(location)
    status = write_status(location, detection)
    return status


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
    
