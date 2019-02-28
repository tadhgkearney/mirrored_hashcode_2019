from slideshow import SlideShow


def make_slides(photo_list):
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
    next_photo = find_next(photo, photo_list, start_index)
    slideshow.add_photo(next_photo)
    photo_list.remove(next_photo)
    add_next(next_photo, slideshow, photo_list, start_index - 1)


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

