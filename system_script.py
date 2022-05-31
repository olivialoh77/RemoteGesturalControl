import os
from multiprocessing import Process, Pipe, Queue
from queue import Empty

#ML 
import ml.ml_script as ml 

#Communications 
import comms.comms as comms 

def main():
   gesture_queue = Queue()

   p_conn, c_conn = Pipe()
   p1 = Process(target=ml.main, args=(p_conn, gesture_queue))
   p2 = Process(target=comms.main, args=(c_conn, gesture_queue))


   p1.start()
   p2.start()
   p3.start()

   #p3.join()
   p2.join()
   p1.join()

if __name__ == '__main__':
    main()