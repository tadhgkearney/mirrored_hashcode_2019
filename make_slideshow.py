from slideshow import SlideShow


def make_slides(photo_list):
    print('Starting slideshow')
    photo_list = list(photo_list)
    photo_list.sort(key=lambda x: int(x.num_tags), reverse=True)
    slideshow = SlideShow()

    first_photo = photo_list.pop()
    slideshow.add_photo(first_photo)
    add_next(first_photo, slideshow, photo_list, len(photo_list)-1)
    return slideshow

def add_next(photo, slideshow, photo_list, start_index):
    if start_index < 0:
        return
    next_photo_index = find_next(photo, photo_list, start_index)
    next_photo = photo_list[next_photo_index]
    slideshow.add_photo(next_photo)
    photo_list[next_photo_index] = None
    while photo_list[start_index] is None:
        start_index -= 1
    add_next(next_photo, slideshow, photo_list, start_index - 1)


def find_next(photo, photo_list, start_index):
    diff = None
    my_photo = start_index - 1
    while my_photo is None:
        start_index -= 1
        my_photo = start_index -1
    while start_index > 0:
        while photo_list[start_index] is None:
            start_index -= 1
        start_index -= 1
        same, diff = get_same_and_different(photo, photo_list[start_index])
        new_diff = abs(same - diff)
        if diff is not None and diff < new_diff:
            diff = new_diff
            my_photo = start_index
            if diff < 50:
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

