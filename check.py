def status(location):
    """ Gets status from the cur.txt associated with location."""
    with open(f'{location}_cur.txt','r') as current_file:
        return current_file.readline()


def timestamp(location):
    """Gets timestamp from the cur.txt associated with location."""
    with open(f'{location}_cur.txt','r') as current_file:
        current_file.readline()
        return current_file.readline()
