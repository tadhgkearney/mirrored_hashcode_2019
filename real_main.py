import merge
import make_slideshow

letter = 'a'

photo_list = merge.merge(letter)
slideshow = make_slideshow.make_slides(photo_list)
slideshow.output(letter)