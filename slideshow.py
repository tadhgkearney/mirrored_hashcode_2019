class SlideShow:
    def __init__(self):
        self._slideShow = []

    def add_photo(self, photo):
        self._slideShow.append(photo)

    def output(self, letter):

        f = open("output/%s" % letter, "a+")

        f.write("%d" % len(self._slideShow))

        for photo in self._slideShow:

            if photo.merged is True:
                f.write("%d %d" % (photo.photo_number[0], photo.photo_number[1]))
            else:
                f.write("%d" % photo.photo_number)

        f.close()


