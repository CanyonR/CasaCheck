import mod
import time

i = int(input("How long should I wait between checking the sensors? Secs: "))

x = 0
while x == 0:
    mod.main()
    time.sleep(i)