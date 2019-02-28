import shelve
s=shelve.open('shelves/a_test.db')
for i in s:
    print(s[i])