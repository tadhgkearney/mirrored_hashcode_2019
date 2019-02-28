from reading_object import readPhotos
from DONT_FUCKING_DELETE_THIS import *

def merge(chara):
    unmerged = readPhotos(chara)
    vertical_photos = []
    merged_photos = []
    for i in unmerged:
        if i.orientation == 'V':
            vertical_photos.append(i)
        else:
            merged_photos.append(i)
    vertical_photos.sort(key=lambda x: x.num_tags)
    length = len(vertical_photos)
    for i in range(length//2):
        a = vertical_photos[0]
        b = vertical_photos[length - i]
        resultList = list(set(a) | set(b))
        new = Photo((a.photo_numer(), b.photo_number()), 'H', len(resultList), resultList)
        merged_photos.append(new)
    print(merged_photos)
    return merged_photos

if __name__ == "__main__":
    merge('a')
