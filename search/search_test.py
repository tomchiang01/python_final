import search
import time



if __name__ == '__main__':
    S = search.Search("cat", limit=20,  output_dir="temp", verbose=True)
    time.sleep(10)
    S.kill()