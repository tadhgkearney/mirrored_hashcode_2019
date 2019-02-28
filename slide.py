class Slide:
    def __init__(self, photo):
        self._photo = photo

    def get_photo(self):
        return self._photo

    def set_photo(self, photo):
        self._photo = photo

    photo = property(get_photo, set_photo)
