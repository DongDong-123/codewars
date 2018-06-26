def nameList(names):
    aa = names[-1]
    bb = names[-2]
    for cc in names[:-2]:
        print(cc['name'])

    return









names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
nameList(names)