import shelve
def readPhotos(letter):
    l=[]
    s=shelve.open('shelves/%s' % (letter))
    for i in s:
        current_photo = s[i]
        l.append(current_photo)

    return l


if __name__=='__main__':
    for photo in(readPhotos('b')):
        print(photo)