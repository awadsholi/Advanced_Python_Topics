from multiprocessing import Pool            #allows to run a function in parallel across multiple input values
import time

def square(x):
    time.sleep(1)
    return  x * x


if __name__ == "__main__":
    with Pool(4) as p:                     #creates a pool of 4 workers processes  ,, "with" that handles opening and closing automatically
        results = p.map(square,[1,2,3,4])
    print(results)

#without Pool the program takes 4 seconds , 1 second per task
#with Pool the program all tasks run at the same tine , 1 second for 4 tasks !!