import merge
import make_slideshow
letters=['b']
for letter in letters:
    print('Starting %s'%letter)
    photo_list = merge.merge(letter)
    slideshow = make_slideshow.make_slides(photo_list)
    slideshow.output(letter)
    print('Done %s'%letter)
