#To simulate a producer that generates data and puts it in a queue(enqueue) amd consumer that takes data (dequeue) and process it (both consumer and producer running in separate threads)

import threading
import queue
import time

q = queue.Queue()                               #is a thread-safe meaning multiple threads can safely put and get items without needing a manual lock

def producer():
    for item in range(5):
        time.sleep(0.5)                         #prducer put item every 0.5 second
        q.put(item)
        print(f"Producer {item}")
    q.put(None)                                 #Put None when reach end as a (sentinel)

def consumer():
    while True:
        item = q.get()                          #run in infinite loop until reach sentinel
        if item is None:
            break
        print(f"Consumed {item}")
        q.task_done()                           #calls this function to signal that the item has been processed

prod_thread =threading.Thread(target=producer)
cons_thread =threading.Thread(target=consumer)

prod_thread.start()
cons_thread.start()

prod_thread.join()
q.join()
cons_thread.join()