from bing_image_downloader.downloader import download


def search(key_word,dir_name,size):
    download(key_word, limit=size,  output_dir=dir_name, adult_filter_off=False, force_replace=False, timeout=60, verbose=False)

if __name__ == "__main__":
    search("cat","temp",10)