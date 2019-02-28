class Photo(object):
    def __init__(self, photo_number, orientation, num_tags, tags):
        self._orientation = orientation
        self._num_tags = num_tags
        self._tags = tags
        self._photo_number = photo_number
        self._merged = False


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

    @property
    def merged(self):
        return self._merged

    def __str__(self):
        return '''Photo Num: %s
Orientation: %s
No of tags: %s
Tags: %s
        '''%(self.photo_number, self.orientation, self.num_tags, self.tags)
