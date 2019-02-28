class SlideShow:
    def __init__(self):
        self._slideShow = []

    def add_photo(self, photo):
        self._slideShow.append(photo)

    def output(self, letter):
        print('Writing output')

        f = open("output/%s" % letter, "w")

        f.writelines("%d\n" % len(self._slideShow))

        for photo in self._slideShow:

            if type(photo.photo_number)==tuple:
                f.writelines("%d %d\n" % (photo.photo_number[0], photo.photo_number[1]))
            else:
                f.writelines("%s\n" % str(photo.photo_number))

        f.close()


