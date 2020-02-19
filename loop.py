import mod
import time

i = int(input("How long should I wait between checking the sensors? Secs: "))

x = True
while x:
    mod.main()
    time.sleep(i)
    