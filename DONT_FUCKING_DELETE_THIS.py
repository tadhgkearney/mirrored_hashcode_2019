'''
    Class representation of a photo
'''
class Photo(object):
    def __init__(self, photo_number, orientation, num_tags, tags):
        '''
        Constructor for Photo object
        :param photo_number: int representing the id of the photo
        :param orientation: Character representing of the orientation of the photo
        :param num_tags: int representing the number of tags a photo has
        :param tags: Array of the tags
        Happy liam? 😠😠😠😠😠😠😠😠😠
        '''
        self._orientation = orientation
        self._num_tags = num_tags
        self._tags = tags
        self._photo_number = photo_number
        self._m = False


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
        return self._m

    def __str__(self):
        return '''Photo Num: %s
Orientation: %s
No of tags: %s
Tags: %s
        '''%(self.photo_number, self.orientation, self.num_tags, self.tags)

if __name__=='__main__':
    p=Photo(213,'H',5,[1,1,2,4]).merged
