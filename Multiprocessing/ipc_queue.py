from multiprocessing import Process, Queue
#Queue--> for safe communication between processes by passing data FIFO

def producer(q):
    q.put("Awad")

def consumer(q):
    print(f"Received: {q.get()}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()