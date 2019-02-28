import shelve
from DONT_FUCKING_DELETE_THIS import Photo
files=['a','b','c','d','e']
for file in files:
    shelve_file =shelve.open('shelves/%s'%(file))
    fin=open('input_files/%s.txt'%(file))
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
            photo=Photo(id,o,num,tags)
            shelve_file[str(id)]=photo
            id+=1
    shelve_file.close()