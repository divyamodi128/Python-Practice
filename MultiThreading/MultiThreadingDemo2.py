from threading import Thread
import time

class AsyncWrite(Thread):
    def __init__(self, txt, filename):
        Thread.__init__(self)
        self.txt = txt
        self.file = filename

    def run(self):
        f = open(self.file, "w")
        f.write(self.txt)
        time.sleep(5)
        f.close()
        print "Finished Writing to", self.file

def CallableFunc():
    msg = raw_input("Enter a String to store:")
    bgprocess = AsyncWrite(msg, "file.txt")
    bgprocess.start()
    print "While the file is written, main process continues"
    print "100 + 200 =", 100 + 200

    # bgprocess.join() # This will wait for the thread to complete
    print "Your file is ready."

CallableFunc()