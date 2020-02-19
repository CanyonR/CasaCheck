import datetime
import random


def timestamp():
    """Generate a timestamp to be used in records."""
     tstamp = datetime.datetime.now().strftime("%Y-%b-%d | %H:%M:%S")
     return tstamp


def mail_sensor():
    """Randomly choose from a list
    (instead of checking the output from physical sensor, as is planned)."""
    opts = [0,1]
    detection = random.choice(opts)
    return detection


def cars_sensor():
    """Randomly choose from a list
    (instead of checking the output from physical sensor, as is planned)."""
    opts = [0,1,2]
    detection = random.choice(opts)
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
        status = cars_sensor_status(detection)
        return status
    else:
        return f"-ERR- location '{location}'"


def determine(location):
    """Return the named status of location based off sensor's detection."""
    detection = read_sensor(location)
    status = write_status(location, detection)
    return status


def log(tstamp, mstat, cstat):
    """Write timestamp and location statuses to a log file."""
    with open('log.txt','a') as log:
        log.write('\n' + tstamp + " | MAIL: " + mstat + " | CARS: " + cstat)


def store(location, status, tstamp):
    """Writes status and timestamp to a "current" file
    for an outside program to reference."""
    with open(f'{location}_cur.txt','w') as cur:
    	cur.write(status + '\n' + tstamp)


def main():
    tstamp = timestamp()
    mstat = determine("mail")
    cstat = determine("cars")
    log(tstamp,mstat,cstat)
    store("mail",mstat,tstamp)
    store("cars",cstat,tstamp)
    # To Be Added: "If 'status' starts with -ERR-, print(status)"