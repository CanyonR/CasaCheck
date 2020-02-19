def status(location):
# Gets status from the cur.txt associated with location
# (passed through from casa.py)
    with open(f'{location}_cur.txt','r') as txt:
        return txt.readline()


def timestamp(location):
# Gets timestamp from the cur.txt associated with location
# (passed through from casa.py)
    with open(f'{location}_cur.txt','r') as txt:
        txt.readline(0)
        return txt.readline()