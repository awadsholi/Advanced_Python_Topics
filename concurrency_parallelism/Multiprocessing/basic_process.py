from multiprocessing import Process                     #this module allows to create separate processes that run concurrently
#Note: Each process can execute a function independently of the main process

def task(name):
    print(f"Process {name} is running")


if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = Process(target=task,args=(f"P{i + 1}",))      #create new process in object p,, target takes the function (task) to be run in a new process
        processes.append(p)
        p.start()                                         #start the process to run task function in a separate process (Isolated)
    for p in processes:
        p.join()                                          #wait the process to finish before continuing