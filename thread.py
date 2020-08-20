import threading
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping')

'''do_something()
do_something()
do_something()
do_something()'''

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t3 = threading.Thread(target=do_something)
t1.start()
t2.start()
t3.start()

# if you want to execute the functions first and 
# then proceed with the further execution of the program use Join() methid
t1.join()
t2.join()
t3.join()
finish = time.perf_counter()

print (f'Finished in {round (finish- start,2)} second(s)')

# above code runs asyncronusly
# for CPU bound tasks, multiprocessing is best option.