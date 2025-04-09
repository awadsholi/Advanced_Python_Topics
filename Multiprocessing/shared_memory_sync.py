from multiprocessing import Process, Value, Lock
#Process to create new Process
#Value to create shared variable between processes
#Lock to prevent race condition
def increment(shared_num, lock):
    for _ in range(1000):
        with lock:                          #Acquires the lock before accessing the shared variable and ensure only one process at a time can update shared value (prevent race condition)
            shared_num.value  += 1          #.value is how accessing the actual value inside a multiprocessing.Value object
if __name__ == "__main__":
    counter = Value('i',0)                  #'i' is for create signed integer variable then initialized by 0
    lock = Lock()                           #creates Lock object
    processes = [Process(target=increment, args= (counter,lock)) for _ in range(4)]         #after creates a list of 4 separate processes each one is set to run the increment() function with shared counter and lock.
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(counter.value)