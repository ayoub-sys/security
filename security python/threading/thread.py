import _thread
import time

def print_epoch(nameOfThread,delay):
    count=0
    while count < 3:
        time.sleep(delay)
        count+=1
        print(nameOfThread,"-------------",time.time())
        
        
_thread.start_new_thread(print_epoch, ("thread1",1))
_thread.start_new_thread(print_epoch,("thread2", 3))
    
