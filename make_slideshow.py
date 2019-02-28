from slideshow import SlideShow


def make_slides(photo_list):
    photo_list = list(photo_list)
    photo_list.sort(key=lambda x: x.num_tags, reverse=True)
    slideshow = SlideShow()
    add_next(photo_list.pop(), slideshow, photo_list, len(photo_list)-1)

def add_next(photo, slideshow, photo_list, start_index):
    pass


def find_next(photo, photo_list, start_index):
    diff = None
    my_photo = photo_list[start_index - 1]
    while start_index > 0:
        start_index -= 1
        same, diff = get_same_and_different(photo, photo_list[start_index])
        new_diff = abs(same - diff)
        if diff is not None and diff < new_diff:
            diff = new_diff
            my_photo = photo_list[start_index]
            if diff < 2:
                return my_photo
    return my_photo




def get_same_and_different(photo, other):
    same = 0
    diff = 0
    for tag in photo.tags:
        if tag in other.tags:
            same += 1
        else:
            diff += 1
    return same, diff

