class Photo(object):
    def __init__(self,orientation,num_tags,tags):
        self._orientation=orientation
        self._num_tags=num_tags
        self._tags=tags

    @property
    def orientation(self):
        return self._orientation

    @property
    def num_tags(self):
        return self._num_tags

    @property
    def tags(self):
        return self._tags

