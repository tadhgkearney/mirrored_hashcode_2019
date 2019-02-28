import shelve
s=shelve.open('shelves/a_test')
for i in s:
    current_photo=s[i]