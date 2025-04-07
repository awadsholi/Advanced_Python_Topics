#Daemon threads automatically exits when main program ends
#regular threads would keep program running indefinitely
#useful for tasks that shouldn't block shutdown (background tasks)
import threading
import time

def background_task():
    while True:
        print("Daemon Threading Running ...")
        time.sleep(0.5)

daemon_thread = threading.Thread(target= background_task,daemon=True)           #daemon threads runs in the background and will terminate when the main program(main thread) finishes

daemon_thread.start()

time.sleep(2)

print("Main program exiting")

#when the main thread finishes, the daemon thread is killed automatically.
#backgrount task runs an infinite loop it doesn't run forever it stops when the main thread (program) ends