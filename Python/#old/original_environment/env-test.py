import os
import time

os.environ['LOADING'] = '1'

while True:
    if 'LOADING' in os.environ:
        print(os.environ['LOADING'])
    else:
        print(123)
    time.sleep(1)
