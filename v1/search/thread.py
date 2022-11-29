from threading import Thread
from time import sleep
import downloader

def run(query, limit, output_dir, adult_filter_off, force_replace, timeout, verbose):
    downloader.download(query, limit=limit,  output_dir=output_dir, adult_filter_off=False, force_replace=False, timeout=5, verbose=verbose)
def run1():
    for x in range(10):
        print("hi")
        sleep(1)
T=Thread(target=run,args=("cat", 10,  "temp", False, False, 5, True, ))
T1=Thread(target=run1)
T.start()
sleep(0.2)
T1.start()
T.join()
T1.join()
print("Bye")