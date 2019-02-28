from reading_object import readPhotos
import DONT_FUCKING_DELETE_THIS

def merge():
    unmerged = readPhotos('a')
    vertical_photos =[]
    merged_photos = []
    for i in unmerged:
        if i._orientation == 'V':
            vertical_photos.append(i)
        else:
            merged_photos.append(i)
    vertical_photos.sort()
    length = range(vertical_photos)
    for i in length:
        a = vertical_list[0]
        b = vertical_list[length - i]
        restultList = list(set(a) | set(b))
        new = Photo((a._photo_numer, b._photo_number), 'H')
    return merged_photos

if __name__ == "__main__":
    merge()