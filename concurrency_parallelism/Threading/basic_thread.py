import threading                                        #import threading module
import time                                             #import time module
def print_numbers():                                    #regular function for thread
    for i in range(3):
        time.sleep(1)                                   #simulate work
        print(f"Number:{i}")

def print_letter():                                     #regular function for thread
    for letter in 'ABC':
        time.sleep(1)
        print(f"Letter: {letter}")


t1 = threading.Thread(target=print_numbers)             #create thread object
t2 = threading.Thread(target=print_letter)


t1.start()                                              #begin thread execution
t2.start()


t1.join()                                               #block main thread until t1 finish
t2.join()



print("All threads Completed")
