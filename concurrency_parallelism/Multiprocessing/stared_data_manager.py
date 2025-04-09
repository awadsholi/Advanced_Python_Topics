from multiprocessing import Process,Manager

#Manager ---> to create shared data structure (list,dict) that can be safely accessed and modified by multiple processes

def add_item(shared_list,item):
    shared_list.append(item)

if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()                #to allow communication and synchronization between processes
        processes = [Process(target=add_item, args=(shared_list,i)) for i in range(3)]      # each process will append a different number to the same shared list
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print(shared_list)