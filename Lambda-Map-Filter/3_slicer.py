def slicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sallly']
print(list(map(slicer, names)))
