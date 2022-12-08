from PIL import Image
import imagehash

def image_hashing(image1, image2):
    hash1 = imagehash.phash(Image.open(image1))
    hash2 = imagehash.phash(Image.open(image2))
    # hash1 = imagehash.phash(image1)
    # hash2 = imagehash.phash(image2)
    print(hash1)
    print(hash1 - hash2)
    return hash1-hash2