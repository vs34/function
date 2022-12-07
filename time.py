import time
a=-1
b=0
while True:
    a = a+1
    print(b,':',a)
    time.sleep(1)
    if a >= 60:
        b = b+1
        a = 0
