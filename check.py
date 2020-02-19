def status(location):
# Gets status from the cur.txt associated with location
# (passed through from main.py)
	with open(f'{location}_cur.txt','r') as cur:
	    mStat = cur.read(5)
	return mStat


def timestamp(location):
# Gets timestamp from the cur.txt associated with location
# (passed through from main.py)
	with open(f'{location}_cur.txt','r') as cur:
	    _x = cur.readline()
	    mTime = cur.readline()
	return mTime