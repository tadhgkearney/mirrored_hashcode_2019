from reading_object import readPhotos
from DONT_FUCKING_DELETE_THIS import *

def merge(chara):
    unmerged = readPhotos(chara)
    vertical_photos = []
    merged_photos = []
    print(unmerged)
    for i in unmerged:
        if i.orientation == 'V':
            vertical_photos.append(i)
        else:
            merged_photos.append(i)
    vertical_photos.sort(key=lambda x: x.num_tags)
    index = len(vertical_photos)-1
    for i in range(len(vertical_photos)//2):
        a = vertical_photos[0]
        b = vertical_photos[index - i]
        resultList = list(set(a.tags) | set(b.tags))
        new = Photo((a.photo_number, b.photo_number), 'H', len(resultList), resultList)
        new.merged = True
        merged_photos.append(new)
    print(merged_photos)
    return merged_photos

if __name__ == "__main__":
    merge('a')
