class Photo(object):
    def __init__(self, photo_number, orientation, num_tags, tags):
        self._orientation = orientation
        self._num_tags = num_tags
        self._tags = tags
        self._photo_number=photo_number

    @property
    def photo_number(self):
        return self._photo_number
    @property
    def orientation(self):
        return self._orientation

    @property
    def num_tags(self):
        return self._num_tags

    @property
    def tags(self):
        return self._tags
