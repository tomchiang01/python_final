import os, sys
import shutil
from pathlib import Path

try:
    from bing import Bing
except ImportError:  # Python 3
    from .bing import Bing


def download(query, limit=100, output_dir='temp', adult_filter_off=True, 
force_replace=False, timeout=60, filter="",black_list=[] , verbose=True):

    # engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    
    image_dir = Path(output_dir).absolute()

    if force_replace:
        if Path.isdir(image_dir):
            shutil.rmtree(image_dir)

    # check directory and create if necessary
    try:
        if not Path.is_dir(image_dir):
            Path.mkdir(image_dir, parents=True)

    except Exception as e:
        print('[Error]Failed to create directory.', e)
        sys.exit(1)
        
    if verbose:
        print("[%] Downloading Images to {}".format(str(image_dir.absolute())))
    bing = Bing(query, limit, image_dir, adult, timeout, filter, black_list, verbose)
    bing.run()


if __name__ == '__main__':
    download("cat", limit=10,  output_dir="temp", adult_filter_off=False, force_replace=False, timeout=5, verbose=True)
