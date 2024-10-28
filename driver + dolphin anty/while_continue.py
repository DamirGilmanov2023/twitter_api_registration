import time
i=0
while i<=9:
    time.sleep(1)
    print('Step1')
    time.sleep(1)
    print('Step2')
    time.sleep(1)
    print(f'i={i}')
    time.sleep(1)
    if i>3:
        #i-=1
        continue
    i+=1
