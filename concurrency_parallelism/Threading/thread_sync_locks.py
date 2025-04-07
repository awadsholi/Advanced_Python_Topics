import threading

counter = 0                                                        #shared variable that all threads will increment
lock = threading.Lock()                                            #mutex lock to ensure that only one thread can access counter at a time (prevent race condition)

def increment_counter():                                           #this function is the task each thread will run
    global counter                                                 #it increments the counter 10000 times
    for _ in range(10000):
        with lock:                                                 #ensures that the increment operation is atomic(one thread can execute at the same time
            counter += 1

threads = []

for _ in range(4):                                                 #creates 4 threads and starts them
    t = threading.Thread(target=increment_counter)                 #each thread runs this function
    threads.append(t)
    t.start()                                                      #thread start execution
for t in threads:
    t.join()                                                       #wait all threads to finish

print(f"Final Counter: {counter}")


#without lock multiple threads may try to read and write counter at the same time leading to incorrect results due to race conditions
