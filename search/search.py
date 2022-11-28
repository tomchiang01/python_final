from threading import Thread

try:
    import downloader
except:
    import search.downloader as downloader

def search(key_word, limit, output_dir, verbose):
    T=Thread(target=downloader.download,args=(key_word, limit,  output_dir, False, False, 5, "", verbose, ))
    T.start()
          

if __name__ == '__main__':
    search("cat", limit=10,  output_dir="temp", verbose=True)
