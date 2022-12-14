from threading import Thread
import multiprocessing
import downloader

class Search:
    def __init__(self,key_word, limit, output_dir, black_list, verbose):
        self.proc = multiprocessing.Process(target=downloader.download,args=(key_word, limit,  output_dir, False, False, 5, "",black_list, verbose, ))
        self.proc.start()
        
    def kill(self):
        self.proc.terminate()
          

if __name__ == '__main__':
    Search("cat", limit=10,  output_dir="temp", verbose=True)
