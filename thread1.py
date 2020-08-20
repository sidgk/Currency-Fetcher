import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping')

'''do_something()
do_something()
do_something()
do_something()'''

#t1 = threading.Thread(target=do_something)
#t2 = threading.Thread(target=do_something)
#t3 = threading.Thread(target=do_something)
#t4 = threading.Thread(target=do_something)
#t5 = threading.Thread(target=do_something)
'''t1.start()
t2.start()
t3.start()

# if you want to execute the functions first and 
# then proceed with the further execution of the program use Join() methid
t1.join()
t2.join()
t3.join()'''
# creating a list because we can use join() within 1st for joop
threads = []
# underscore '_' is a throwaway variable. 
for _ in range(10):
    t = threading.Thread(target=do_something, args = [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print (f'Finished in {round (finish- start,2)} second(s)')

