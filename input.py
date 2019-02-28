import shelve
from DONT_FUCKING_DELETE_THIS import Photo

shelve_file =shelve.open('shelves/a_test')
fin=open('input_files/a_example.txt')
id=0
c=False
for line in fin.readlines():
    if not c:
        c=True
        continue
    else:
        l=line.split()
        o=l[0]
        num=l[1]
        tags=l[2:]
        photo=Photo(o,num,tags)
        shelve_file[str(id)]=photo
        id+=1
shelve_file.close()