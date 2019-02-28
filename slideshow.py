class SlideShow:
    def __init__(self):
        self._slideShow = []

    def add_photo(self, photo):
        self._slideShow.append(photo)

    def output(self, letter):

        f = open("output/%s" % letter, "w")

        f.writelines("%d\n" % len(self._slideShow))

        for photo in self._slideShow:
            print(photo.photo_number)

            if photo.merged:
                f.writelines("%d %d\n" % (photo.photo_number[0], photo.photo_number[1]))
            else:
                f.writelines("%s\n" % str(photo.photo_number))

        f.close()


